# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask App running via DevOps CI/CD!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Fallback to 5000 if PORT not set
    app.run(host="0.0.0.0", port=port)

