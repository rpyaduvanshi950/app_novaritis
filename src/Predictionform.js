import React, { useState, useEffect } from "react";
import M from "materialize-css";

const PredictionForm = () => {
  const [formData, setFormData] = useState({
    durationOfTrial: "",
    enrollment: "",
    primaryCompletionDuration: "",
    mergeOutcome: "",
    studyResults: "",
    conditions: "",
  });

  const [prediction, setPrediction] = useState("");

  useEffect(() => {
    M.AutoInit();
    M.updateTextFields();
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const response = await fetch("/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    });

    const data = await response.json();
    setPrediction(data.prediction);
  };

  return (
    <div className="container">
      <h1 className="header center orange-text">Prediction Model</h1>
      <h5 className="header center light">Prediction of Recruitment Rate</h5>

      <form onSubmit={handleSubmit} className="row">
        {/* Row 1 */}
        <div className="input-field col s4">
          <input
            id="durationOfTrial"
            name="durationOfTrial"
            type="text"
            value={formData.durationOfTrial}
            onChange={handleChange}
            className="validate"
          />
          <label htmlFor="durationOfTrial">Duration of Trial</label>
        </div>

        <div className="input-field col s4">
          <input
            id="enrollment"
            name="enrollment"
            type="text"
            value={formData.enrollment}
            onChange={handleChange}
            className="validate"
          />
          <label htmlFor="enrollment">Enrollment</label>
        </div>

        <div className="input-field col s4">
          <input
            id="primaryCompletionDuration"
            name="primaryCompletionDuration"
            type="text"
            value={formData.primaryCompletionDuration}
            onChange={handleChange}
            className="validate"
          />
          <label htmlFor="primaryCompletionDuration">Primary Completion Duration</label>
        </div>

        <div className="input-field col s4">
          <input
            id="mergeOutcome"
            name="mergeOutcome"
            type="text"
            value={formData.mergeOutcome}
            onChange={handleChange}
            className="validate"
          />
          <label htmlFor="mergeOutcome">Merged Outcomes</label>
        </div>

        <div className="input-field col s4">
          <input
            id="studyResults"
            name="studyResults"
            type="text"
            value={formData.studyResults}
            onChange={handleChange}
            className="validate"
          />
          <label htmlFor="studyResults">Study Results</label>
        </div>

        <div className="input-field col s4">
          <input
            id="conditions"
            name="conditions"
            type="text"
            value={formData.conditions}
            onChange={handleChange}
            className="validate"
          />
          <label htmlFor="conditions">Conditions</label>
        </div>

        <div className="row center">
          <button type="submit" className="btn-large waves-effect waves-light orange">
            Predict Recruitment Rate
          </button>
        </div>
      </form>

      {prediction && (
        <div className="center">
          <h5 className="orange-text">Prediction: {prediction}</h5>
        </div>
      )}
    </div>
  );
};

export default PredictionForm;
