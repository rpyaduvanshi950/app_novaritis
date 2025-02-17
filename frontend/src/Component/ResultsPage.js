import React from "react";
import { useNavigate, useLocation } from "react-router-dom";

const ResultsPage = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const finalData = location.state?.finalData;

  const renderFinalData = () => {
    if (!finalData || finalData.length === 0) return <p>No data to display.</p>;

    const keys = Object.keys(finalData[0]);

    return (
      <table className="highlight">
        <thead>
          <tr>
            {keys.map((key) => (
              <th key={key}>{key}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {finalData.map((row, index) => (
            <tr
              key={index}
              className={index % 2 === 0 ? 'even-row' : 'odd-row'}
              style={{
                animation: 'fadeIn 0.5s ease-out forwards',
                animationDelay: `${index * 0.1}s`,
                opacity: 0,
              }}
            >
              {keys.map((key) => (
                <td key={key}>{row[key]}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    );
  };

  const handleGoBack = () => {
    navigate("/");
  };

  return (
    <div className="container">
      <h5 className="header center orange-text">Processed Data</h5>

      <div className="row center"   >
        <button
          className="btn-large waves-effect waves-light orange" 
          style={{
            display:'flex',
            flexDirection:'row',
            justifyContent:'space-between',
            alignItems:'center',
            gap:'20px'
          }}
          onClick={handleGoBack}
        >
          <span className="material-icons">arrow_back</span> Back to Upload
        </button>
      </div>

      <div className="row center">
        {renderFinalData()}
      </div>

      <style>
        {`
          /* Remove hover effect for table rows */
          .odd-row:hover {
            background-color: inherit; /* Disable the hover effect */
          }

          /* Animation for fading in rows */
          @keyframes fadeIn {
            0% {
              opacity: 0;
              transform: translateY(20px);
            }
            100% {
              opacity: 1;
              transform: translateY(0);
            }
          }

          /* Define different colors for even and odd rows */
          .even-row {
            background-color: white;
            color: black;
          }

          .odd-row {
            background-color: rgb(169, 169, 169); /* Light gray background */
            color: white; /* White text */
          }

          /* Style for headings to make them gray */
          th {
            background-color: rgb(169, 169, 169); /* Gray background for headings */
            color: black; /* Black text for headings */
          }
        `}
      </style>
    </div>
  );
};

export default ResultsPage;
