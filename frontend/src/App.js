import React, { useState } from "react";
import PredictionForm from "./Predictionform";

const App = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState("");

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleFileUpload = async () => {
    if (!selectedFile) {
      setUploadStatus("Please select a file before uploading.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await fetch("/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setUploadStatus(`File uploaded successfully!`);
    } catch (error) {
      setUploadStatus("Error uploading file. Please try again.");
    }
  };

  return (
    <div>
      <nav className="light-blue lighten-1">
        <div className="nav-wrapper container">
          <a href="#" className="brand-logo">NOVARTIS</a>
          <ul className="right hide-on-med-and-down">
            <li><a href="https://clinicaltrials.gov/">Data Source</a></li>
          </ul>
        </div>
      </nav>

      <PredictionForm />

      <div className="container center">
        <h5 className="grey-text">OR</h5>
      </div>


      <div className="container">
        <h5 className="header center orange-text">Upload File for Batch Prediction</h5>

        <div className="row center">
          <div className="file-field input-field col s6 offset-s3">
            <div className="btn orange">
              <span>Upload File</span>
              <input type="file" accept=".csv, .xlsx" onChange={handleFileChange} />
            </div>
            <div className="file-path-wrapper">
              <input className="file-path validate" type="text" placeholder="Upload a CSV or XLSX file" />
            </div>
          </div>
        </div>

        <div className="row center">
          <button className="btn-large waves-effect waves-light orange" onClick={handleFileUpload}>
            Predict from File
          </button>
        </div>

        {uploadStatus && (
          <div className="row center">
            <h6 className="green-text">{uploadStatus}</h6>
          </div>
        )}
      </div>

      {/* Footer
      <footer className="page-footer orange">
        <div className="container">
          <div className="row">
            <div className="col l6 s12">
              <h5 className="white-text">Company Bio</h5>
              <p className="grey-text text-lighten-4">
                We are a team of college students working on this project like it's our full-time job.
              </p>
            </div>
          </div>
        </div>
      </footer> */}
    </div>
  );
};

export default App;
