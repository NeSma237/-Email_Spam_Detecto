# 📧 Email Spam Classifier with Streamlit

This project is a **machine learning-powered email spam classifier** built using a `RandomForestClassifier` and deployed with **Streamlit**. The app allows users to input email text and get instant classification as `spam` or `ham`.

---

## 🚀 Features

- Text preprocessing: lowercasing, punctuation removal, stopword filtering, and lemmatization.
- TF-IDF vectorization of email content.
- Trained on the Enron Spam dataset.
- Deployed using Streamlit Community Cloud.

---

## 🧠 Model Details

- Algorithm: Random Forest Classifier  
- Vectorizer: TF-IDF (max 5000 features)  
- Preprocessing: NLTK-based cleaning an

pip install -r requirements.txt
Run the app:

streamlit run app.py

##☁️ Deployed Version
Try the live app here:
👉 [https://your-streamlit-url.streamlit.app](https://jplrzwj4bqrrbyx5km6nua.streamlit.app/)

--email-spam-classifier/
--│
--├── app.py                     # Streamlit app interface
--├── spam_classifier_model.pkl.gz  # Compressed trained model
--├── tfidf_vectorizer.pkl       # TF-IDF vectorizer
--├── requirements.txt           # Dependencies
--└── README.md                  # Project overview

🧑‍💻 Authors
Made with ❤️ by 
Arwa Salim
Nourhan Ibrahim
Fajr Abo Bakr
Nesma Nasser
