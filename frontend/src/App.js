import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";  
import UploadPage from "./Component/UploadPage";
import ResultsPage from "./Component/ResultsPage";
import Logo from './Assets/logo.png'
const App = () => {
  return (
    <div>
      <nav className="light-blue lighten-1">
         <div className="nav-wrapper container">
           {/* <a href="#" className="brand-logo">NOVARTIS</a> */}
           <img src={Logo} alt="Logo" className="brand-logo" style={{width:'200px', paddingTop:'12px'}} />
           <ul className="right hide-on-med-and-down">
           <li><a href="https://clinicaltrials.gov/">Data Source</a></li>
           </ul>
         </div>
     </nav>
    <Router>

      <Routes>
        <Route path="/" element={<UploadPage />} />
        <Route path="/results" element={<ResultsPage />} />
      </Routes>
    </Router>
    </div>

  );
};

export default App;
