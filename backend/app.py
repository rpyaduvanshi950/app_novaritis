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
    file_save_path = os.path.join(uploads_dir, "data.xlsx")
    file.save(file_save_path)
    print("File saved to:", file_save_path)

# flag is added to directly print the output of the test file without buffering
    process = subprocess.Popen(["python3", "-u", "test.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
     # Check if the `test.py` script generated the final_data variable
    try:
        # Assuming test.py stores final_data as a global variable
        import test  # Importing test.py here to access the final_data
        final_data = test.final_data
    except Exception as e:
        print("Error importing final_data:", e)

    # Check if final_data is a DataFrame, and convert it to a serializable format
    if isinstance(final_data, pd.DataFrame):
        # Convert DataFrame to dictionary or JSON serializable format
        final_data = final_data.to_dict(orient="records")  # Convert to a list of dicts

    # Return the final_data as part of the response
    if final_data is not None:
        return jsonify({"message": "File uploaded and processed successfully", "final_data": final_data}), 200
    else:
        return jsonify({"message": "File uploaded but no data was processed"}), 200

    # return jsonify({"message": "File uploaded successfully"}), 200

@app.route('/')
def hello_world():
    return send_from_directory(app.static_folder, 'index.html' )

if __name__ == '__main__':
    app.run(debug=True)
 