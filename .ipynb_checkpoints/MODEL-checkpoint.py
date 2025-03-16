import tkinter as tk
from tkinter import messagebox
import joblib  # Or pickle, depending on how your model is saved
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# Load the trained model and vectorizer
MODEL_PATH = "language_model.pkl"  # Update with your actual model filename
VECTORIZER_PATH = "vectorizer.pkl"

model = joblib.load(MODEL_PATH)
cv = joblib.load(VECTORIZER_PATH)

def predict_language():
    text = entry.get()
    if not text:
        messagebox.showerror("Error", "Please enter some text!")
        return
    
    user_data = cv.transform([text]).toarray()
    predicted_class = model.predict(user_data)[0]
    
    label_result.config(text=f"Predicted Language: {predicted_class}")

# GUI
root = tk.Tk()
root.title("Language Predictor")
root.geometry("400x200")

tk.Label(root, text="Enter text:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Predict Language", command=predict_language).pack(pady=10)
label_result = tk.Label(root, text="Prediction will appear here", font=("Arial", 12))
label_result.pack(pady=10)

root.mainloop()
