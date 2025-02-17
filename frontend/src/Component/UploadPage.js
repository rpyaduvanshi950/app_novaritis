import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import Loader from "./Loader";  

const UploadPage = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState("");
  const [loadingMessage, setLoadingMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false); 
  const navigate = useNavigate();

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleFileUpload = async () => {
    if (!selectedFile) {
      setUploadStatus("Please select a file before uploading.");
      return;
    }

    setIsLoading(true);
    setLoadingMessage("Predictions are being made...");

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await fetch("/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      if (data.final_data) {
        setLoadingMessage("Redirecting to the result...");

        setTimeout(() => {
          navigate("/results", { state: { finalData: data.final_data } });
        }, 2000); 
      } else {
        setUploadStatus("No data was processed.");
        setIsLoading(false);
      }
    } catch (error) {
      setUploadStatus("Error uploading file. Please try again.");
      setIsLoading(false); 
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="header center orange-text" style={{ paddingTop: "50px" }}>
        Prediction Model
      </h1>
      <h5 className="header center light" style={{ paddingBottom: "20px" }}>
        Prediction of Recruitment Rate
      </h5>
      <h5 className="header center orange-text" style={{ paddingBottom: "20px" }}>
        Upload File for Batch Prediction
      </h5>

      <div
        className="row center"
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          gap: "20px",
        }}
      >
        <div className="file-field input-field s6">
          <div
            className="btn orange"
            style={{
              width: "15vw",
              display: "flex",
              flexDirection: "column",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <span>Upload File</span>
            <input type="file" accept=".csv, .xlsx" onChange={handleFileChange} />
          </div>
          <div className="file-path-wrapper">
            <input
              className="file-path validate"
              type="text"
              placeholder="Upload a CSV or XLSX file"
            />
          </div>
        </div>
      </div>

      <div className="row center">
        <button
          className="btn-large waves-effect waves-light orange"
          onClick={handleFileUpload}
        >
          Predict from File
        </button>
      </div>

      {uploadStatus && (
        <div className="row center">
          <h6 className="green-text">{uploadStatus}</h6>
        </div>
      )}

      {/* Conditionally render the loader */}
      {isLoading && <Loader message={loadingMessage} />}
    </div>
  );
};

export default UploadPage;
