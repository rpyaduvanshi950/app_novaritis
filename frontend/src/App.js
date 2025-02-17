import React, { useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";  
import UploadPage from "./Component/UploadPage";
import ResultsPage from "./Component/ResultsPage";
import Logo from './Assets/logo.png'
import Navbar from "./Component/Navbar";
import Footer from "./Component/Footer";
const App = () => {
  return (
    <div>
      <div>
      <Navbar />
      </div>
    <Router>
      <Routes>
        <Route path="/" element={<UploadPage />} />
        <Route path="/results" element={<ResultsPage />} />
      </Routes>
    </Router>
    {/* <Footer /> */}
    </div>

  );
};

export default App;
