import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [joke, setJoke] = useState('');

  const fetchJoke = async () => {
    const response = await fetch('https://joke-app-4.onrender.com/joke');
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
