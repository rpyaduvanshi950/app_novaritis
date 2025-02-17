import React, { useEffect, useState } from 'react';
import '../Assets/style.css';

const Loader = ({ message }) => {
  const [isFadingOut, setIsFadingOut] = useState(false);

  useEffect(() => {
    if (message === "Redirecting to the result...") {
      setTimeout(() => {
        setIsFadingOut(true);
      }, 1800); 
    }
  }, [message]);

  return (
    <div className={`loader-overlay ${isFadingOut ? 'fade-out' : ''}`}>
      <div className="loader-box">
        <div className="loader">
          <span className="loader-text">{message}</span>
          <span className="load"></span>
        </div>
      </div>
    </div>
  );
};

export default Loader;
