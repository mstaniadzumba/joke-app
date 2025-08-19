import React, { useState, useEffect } from 'react';

function App() {
  const [joke, setJoke] = useState('');

  const fetchJoke = async () => {
    const response = await fetch('http://127.0.0.1:5000/joke'); // your Flask endpoint
    const data = await response.json();
    setJoke(`${data.setup} ${data.punchline}`);
  };

  useEffect(() =>{
    fetchJoke();
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>Random Joke Generator</h1>
      <button onClick={fetchJoke}>Get Joke</button>
      <p>{joke}</p>
    </div>
  );
}
 
export default App;
