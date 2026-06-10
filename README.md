# 🛡️ Spam Mail & SMS Detector (ML Model + Web App)

A complete end-to-end machine learning project that classifies SMS messages and emails as either **Spam** or **Ham** (Safe). 

This project includes the full model training pipeline (handling imbalanced data, text preprocessing) and a fully functional, modern web application built with Flask for users to test the models in real-time.

---

## 🧠 Part 1: Machine Learning Models

The core of this project relies on Natural Language Processing (NLP) and supervised machine learning algorithms to filter unwanted spam messages automatically.

### Dataset Overview
- **Source:** [Kaggle – SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- **Records:** 5,572 SMS messages
- **Target Variable:** Spam (`1`) / Ham (`0`)

### ML Pipeline & Workflow
1. **Data Preprocessing:** Removed null values, replaced missing values with empty strings, and encoded labels.
2. **Text Cleaning:** Applied tokenization, stop-word removal, and stemming (PorterStemmer) using NLTK.
3. **Feature Extraction:** Applied **TF-IDF Vectorization** to convert text messages into numerical feature vectors.
4. **Handling Imbalanced Data:** Used **SMOTE** (Synthetic Minority Over-sampling Technique) to balance the spam and ham classes in the training dataset, preventing model bias towards the majority class.
5. **Model Building:** Trained and compared two separate classifiers (Logistic Regression and SVM).

### 📊 Model Performance & Evaluation

Both models performed exceptionally well, with **SVM** showing a slight edge in identifying spam messages (higher Precision and F1-score).

#### 1. Support Vector Machine (SVM) - *Top Performing Model*
* **Training Accuracy:** 99.75%
* **Testing Accuracy:** 98.57%
* **Spam Detection (Test Set):**
  * Precision: 0.97
  * Recall: 0.92
  * F1-Score: 0.95
* *Confusion Matrix (Test):* 956 True Negatives, 143 True Positives, 4 False Positives, 12 False Negatives.

#### 2. Logistic Regression
* **Training Accuracy:** 98.86%
* **Testing Accuracy:** 97.85%
* **Spam Detection (Test Set):**
  * Precision: 0.94
  * Recall: 0.90
  * F1-Score: 0.92
* *Confusion Matrix (Test):* 951 True Negatives, 140 True Positives, 9 False Positives, 15 False Negatives.

### Output Files
The trained models and the TF-IDF vectorizer were combined and serialized into a single dictionary file for easy deployment:
- `spam_models.pkl` (Contains `logistic_model`, `svm_model`, and `vectorizer`)

---

## 💻 Part 2: Web Application

To make the models accessible, they were integrated into a responsive, user-friendly web interface.

### ✨ Web App Features
- **Algorithm Selection:** Users can dynamically switch between the **SVM** and **Logistic Regression** models using a dropdown menu to compare predictions.
- **Real-time Processing:** Uses NLTK in the backend to clean the user's input exactly as it was done during training, before vectorizing and predicting.
- **Modern UI/UX:** A clean, glassmorphism-inspired interface with responsive design.
- **Dark/Light Mode:** Includes a fully functional theme toggle (saves user preference in LocalStorage).

### 🛠️ Technologies Used
- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn, NumPy, Pandas, Imbalanced-learn (SMOTE)
- **NLP Library:** NLTK (Natural Language Toolkit)
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
