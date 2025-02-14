import os
import shutil
import subprocess
import pickle
import pandas as pd
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from test import process_file  # using test.py as is

app = Flask(__name__, static_folder="../frontend/build", static_url_path="")
CORS(app)

# Load your ML model
model_path = os.path.join(os.path.dirname(__file__), "gbm_model.pkl")
with open(model_path, "rb") as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.get_json()
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    return jsonify({"prediction": prediction})

@app.route('/upload', methods=['POST'])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    # Saves the file to an "uploads" directory.
    uploads_dir = os.path.join(os.path.dirname(__file__), "uploads")
    os.makedirs(uploads_dir, exist_ok=True)
    file_save_path = os.path.join(uploads_dir, file.filename)
    file.save(file_save_path)

    relative_target_path = os.path.join(os.path.dirname(__file__), "Use_Case_4 Test_dataset_To be shared.xlsx")
    shutil.copy(file_save_path, relative_target_path)

    content_dir = os.path.join(os.path.dirname(__file__), "content")
    os.makedirs(content_dir, exist_ok=True)
    symlink_path = os.path.join(content_dir, "filedata.xlsx")
    if os.path.lexists(symlink_path):
        os.remove(symlink_path)
    os.symlink(relative_target_path, symlink_path)

    if file.filename.endswith(".csv"):
        df = pd.read_csv(relative_target_path)
    elif file.filename.endswith((".xlsx", ".xls")):
        df = pd.read_excel(relative_target_path, engine="openpyxl")
    else:
        return jsonify({"error": "Unsupported file type"}), 400

    # this runs the model script
    result = subprocess.run(["python", "test.py"], capture_output=True, text=True)
    print("Output from test.py:")
    print(result.stdout)
    print(result.stderr)

    predictions = model.predict(df)
    print("Predictions from model:")
    print(predictions)

    return jsonify({"message": "File processed and predictions made."})

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)