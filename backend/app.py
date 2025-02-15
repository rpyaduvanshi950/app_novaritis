from flask import Flask, send_from_directory, request, jsonify
import os
import shutil
import subprocess
import pickle
import pandas as pd
from flask_cors import CORS


app = Flask(__name__,static_folder="../frontend/build", static_url_path='')   
CORS(app)

# loads the model
model_path = os.path.join(os.path.dirname(__file__), "content/gbm_model.pkl")
with open(model_path, "rb") as file:
    model = pickle.load(file)

@app.route('/upload', methods=['POST'])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]

    uploads_dir = os.path.join(os.path.dirname(__file__), "content")
    os.makedirs(uploads_dir, exist_ok=True)
    file_save_path = os.path.join(uploads_dir, file.filename)
    file.save(file_save_path)
    print("File saved to:", file_save_path)

    process = subprocess.Popen(["python3", "test.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Process started")

    return jsonify({"message": "File uploaded successfully"}), 200

@app.route('/')
def hello_world():
    return send_from_directory(app.static_folder, 'index.html' )

if __name__ == '__main__':
    app.run(debug=True)