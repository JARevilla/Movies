import React from 'react';
import '../App.css';

function Result({ result }) {
  return (
    <div className="result-item">
      <img src={result.imgSrc} alt={result.title} />
      <div>
        <p><strong>Title:</strong> {result.title}</p>
        <p><strong>Page:</strong> <a href={result.link} target="_blank" rel="noopener noreferrer">{result.link}</a></p>
      </div>
    </div>
  );
}

export default Result;
