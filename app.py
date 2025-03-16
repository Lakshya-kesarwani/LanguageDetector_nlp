from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES
import joblib
import asyncio

app = Flask(__name__)
MODEL_PATH = "language_model.pkl"  # Update with your actual model filename
VECTORIZER_PATH = "vectorizer.pkl"

model = joblib.load(MODEL_PATH)
cv = joblib.load(VECTORIZER_PATH)

def predict_language(text):
    user_data = cv.transform([text]).toarray()
    predicted_class = model.predict(user_data)[0]
    print(predicted_class)
    return predicted_class
async def detect_and_translate(text, target_lang):
    # Detect language
    result_lang = predict_language(text)

    # Translate language
    translator = Translator()
    translate_text = await translator.translate(text, dest=target_lang)
    print(translate_text.text)

    return result_lang, translate_text.text


@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)


@app.route('/trans', methods=['POST'])
def trans():
    translation = ""
    detected_lang = ""
    text=" "
    if request.method == 'POST':
        text = request.form['text']
        target_lang = request.form['target_lang']
        detected_lang, translation = asyncio.run(detect_and_translate(text, target_lang))

    return render_template('index.html', translation=translation, detected_lang=detected_lang, languages=LANGUAGES,text=text)


if __name__ == '__main__':
    app.run(debug=True)