import string
from typing import Union
from fastapi import FastAPI
from collections import Counter


app = FastAPI()

@app.get("/")
async def read_root():
    return { "message": "Welcome to text analyzer app!"}

@app.post("/analyze")
async def analyze_text(text: str):
    words = text.split()
    wc = len(words)
    
    # the most common letter
    letters = [char.lower() for char in text if char.isalpha()]
    most_commot_letter = Counter(letters).most_common(1)[0][0] if letters else None
    
    return {
        "word_count": wc,
        "most_common_letter": most_commot_letter
    }
    
