import React, { useEffect, useState } from 'react';

function App() {
  const [nome, setNome] = useState('');
  const [sobrenome, setSobrenome] = useState('');

  useEffect(() => {
    fetch('/react')
      .then(response => response.json())
      .then(data => {
        setNome(data.flask_token.nome);
        setSobrenome(data.flask_token.sobrenome);
      });
  }, []);

  return (
    <div>
      <h1>{nome} {sobrenome}</h1>
    </div>
  );
}

export default App;
