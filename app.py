import streamlit as st
import joblib
import re, string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# تحميل الموارد المطلوبة
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# تحميل النموذج والـ vectorizer
import gzip
with gzip.open("spam_classifier_model.pkl.gz", "rb") as f:
    model = joblib.load(f)
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# دوال تنظيف النص
def clean_message(message):
    message = str(message).lower()
    message = re.sub(f"[{re.escape(string.punctuation)}]", "", message)
    message = re.sub(r"\d+", "", message)
    message = re.sub(r"\s+", " ", message).strip()
    return message

def preprocess_message(message):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))

    message = clean_message(message)
    tokens = message.split()
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]

    return " ".join(tokens)

# واجهة Streamlit
st.title("📧 Email Spam Classifier")
st.write("اكتب الإيميل وهقولك إذا كان Spam ولا Ham 😉")

user_input = st.text_area("✉️ محتوى الإيميل:")

if st.button("🔍 تصنيف"):
    if user_input.strip() == "":
        st.warning("من فضلك اكتب محتوى الإيميل الأول.")
    else:
        cleaned_input = preprocess_message(user_input)
        vectorized_input = vectorizer.transform([cleaned_input])
        prediction = model.predict(vectorized_input)[0]
        st.success(f"🔎 تم تصنيفه كـ: **{prediction.upper()}**")
