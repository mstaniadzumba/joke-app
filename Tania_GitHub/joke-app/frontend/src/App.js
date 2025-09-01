import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [joke, setJoke] = useState('');

  const fetchJoke = async () => {
    const response = await fetch('http://127.0.0.1:5000/joke');
    const data = await response.json();
    setJoke(`${data.setup} ${data.punchline}`);
  };

  useEffect(() =>{
    fetchJoke();
  }, []);

  return (
    <div className="app">
      <h1>Random Joke Generator</h1>
      <div className="joke-box">
        <p>{joke}</p>
      </div>
      <button className="joke-button" onClick={fetchJoke}>
        Get Joke
      </button>
    </div>
  );
}
 
export default App;
