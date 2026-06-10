from flask import Flask, render_template, request
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

app = Flask(__name__)

with open("spam_models.pkl", "rb") as file:
    data = pickle.load(file)

logistic_model = data["logistic_model"]
svm_model = data["svm_model"]
vectorizer = data["vectorizer"]

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

@app.route('/')
def home():
    return render_template('index.html', selected_model='svm')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        model_choice = request.form['model_choice'] 

        processed_message = preprocess_text(message)

        vectorized_message = vectorizer.transform([processed_message])

        if model_choice == 'logistic':
            prediction = logistic_model.predict(vectorized_message)
            model_name_display = "Logistic Regression"
        else:
            prediction = svm_model.predict(vectorized_message)
            model_name_display = "Support Vector Machine (SVM)"

        result = "Spam" if prediction[0] == 1 else "Ham"

        return render_template('index.html',
                               prediction_text=f'This message is: {result}',
                               original_text=message,
                               selected_model=model_choice,  
                               model_name=model_name_display)  

if __name__ == '__main__':
    app.run(debug=True)
