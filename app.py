from flask import Flask, render_template, request
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Make sure NLTK dependencies are downloaded
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

app = Flask(__name__)

# Load BOTH models and the vectorizer
with open("spam_models.pkl", "rb") as file:
    data = pickle.load(file)

logistic_model = data["logistic_model"]
svm_model = data["svm_model"]
vectorizer = data["vectorizer"]

# Recreate the exact preprocessing function used during training
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', ' ', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    words = [ps.stem(word) for word in words]
    return " ".join(words)

# Route for the home page
@app.route('/')
def home():
    # Default to SVM when page first loads
    return render_template('index.html', selected_model='svm')

# Route for prediction when user submits the form
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        model_choice = request.form['model_choice']  # Get the user's choice from the dropdown

        # 1. Preprocess the input
        processed_message = preprocess_text(message)

        # 2. Vectorize
        vectorized_message = vectorizer.transform([processed_message])

        # 3. Predict using the chosen model
        if model_choice == 'logistic':
            prediction = logistic_model.predict(vectorized_message)
            model_name_display = "Logistic Regression"
        else:
            prediction = svm_model.predict(vectorized_message)
            model_name_display = "Support Vector Machine (SVM)"

        # 4. Format result (1 = Spam, 0 = Ham)
        result = "Spam" if prediction[0] == 1 else "Ham"

        return render_template('index.html',
                               prediction_text=f'This message is: {result}',
                               original_text=message,
                               selected_model=model_choice,  # Keeps the dropdown on what they picked
                               model_name=model_name_display)  # Sends the name to show in the results

if __name__ == '__main__':
    app.run(debug=True)