import React, { useState, useEffect } from "react";
import axios from "axios";
import { Table } from "react-bootstrap";

const ListaConvidados = () => {
  const [convidados, setConvidados] = useState([]);
  const [nome, setNome] = useState("");
  const [participacao, setParticipacao] = useState(undefined);

  useEffect(() => {
    const fetchConvidados = async () => {
      const response = await axios.get("/listar/convidado", {
        params: { nome, participacao },
      });
      setConvidados(response.data);
    };

    fetchConvidados();
  }, [nome, participacao]);

  return (
    <>
      <h1>Lista de Convidados</h1>
      <div>
        <label htmlFor="nome">Nome:</label>
        <input
          id="nome"
          type="text"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
        />
      </div>
      <div>
      <label htmlFor="participacao">Já participou:</label>
        <select
          id="participacao"
          value={participacao ?? ""}
          onChange={(e) => setParticipacao(e.target.value === "true")}
        >
          <option value="">Todos</option>
          <option value="true">Sim</option>
          <option value="false">Não</option>
        </select>
      </div>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Já participou</th>
          </tr>
        </thead>
        <tbody>
          {convidados.map((convidado) => (
            <tr key={convidado.id}>
              <td>{convidado.id}</td>
              <td>{convidado.nome}</td>
              <td>{convidado.ja_participou ? "Sim" : "Não"}</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </>
  );
};

export default ListaConvidados;
