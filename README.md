# Language Detector and Translator Web App

This project is a **language detection and translation web application** built using **Flask, NLP, and Machine Learning**. It can detect **22 different languages** using an **ML model trained with Multinomial Naïve Bayes** and translate text into **[INSERT NUMBER] languages** using **Google Translate API**.

## Features
- **Language Detection**: Detects text written in one of the 22 trained languages.
- **Translation**: Translates the detected text into **245 available languages**.
- **Web Interface**: Simple and interactive web interface using Flask.
- **Deployed on Render**: Available at **[https://langdetect-yoxq.onrender.com/](https://langdetect-yoxq.onrender.com/)**.

## Trained Languages for Detection
- Arabic, Chinese, Dutch, English, Estonian, French, Hindi, Indonesian, Japanese, Korean, Latin, Persian, Portuguese, Pashto, Romanian, Russian, Spanish, Swedish, Tamil, Thai, Turkish, Urdu.

## Deployment & Usage
### 1. Clone the Repository
```bash
git clone https://github.com/Lakshya-kesarwani/LanguageDetector_nlp.git
cd LanguageDetector_nlp
```

### 2. Install Dependencies
Ensure you have **Python 3.7+** installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Run the Flask App
```bash
python app.py
```
The app will start running at `http://127.0.0.1:5000/`.

---

## Project Structure

```
LanguageDetector_nlp/
│── static/            # CSS, JS, Images
│── templates/         # HTML Templates
│── language_model.pkl # Trained ML Model
│── vectorizer.pkl     # NLP Vectorizer
│── app.py             # Flask Application
│── requirements.txt   # Dependencies
│── language.csv       # Dataset Used
│── MODEL.ipynb        # Model Training Notebook
```

---

## Contributing

Feel free to fork the repo and enhance the model or UI! Pull requests are welcome.

---

### Author

**Lakshya Kesarwani**

