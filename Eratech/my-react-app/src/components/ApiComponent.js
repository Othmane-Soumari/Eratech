import React, { useState, useEffect } from 'react';

const ApiComponent = () => {
  const [data, setData] = useState({});

  useEffect(() => {
    fetch('http://localhost:8000/api/data')
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.error('Error:', error));
  }, []);

  return (
    <div>
      <h2>Réponse de l'API FastAPI :</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

export default ApiComponent;
