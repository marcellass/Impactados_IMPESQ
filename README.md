<h2>Sprint: </h2>

<h4>Fora da imagem/No dockerplay</h4>
<ul>
  <li> git clone https://github.com/marcellass/Impactados_IMPESQ - clonar o projeto no Github</li>
  <li> git pull - para baixar o projeto do Github atualizado </li>
  <li> git push - para mandar atualização para o Github</li>
  <li> docker-compose down - ele derruba o docker e apaga tudo</li>
  <li> docker-compose up -d - ele inicia o docker</li>
  <h5>Caso quiser atualizar algum arquivo e rodar novamente, não precisa dar o down(apaga tudo), basta dar o stop e o start</h5>
  <li> docker-compose stop - ele somente para o docker</li>
  <li> docker-compose start - starta com as atualizações feitas </li>
  <li> docker exec -it <id do container> /bin/bash - entrar dentro da imagem </li>
  <li> docker-compose down --rmi all - da o down e remove todas as imagens</li>
</ul>

<h4>Dentro da imagem</h4>
<ul>
  <li> mysql -uroot -p - entrar no banco </br>
       senha: impactados</li>
  <li> create schema pesquisa; - criar banco </li>
  <li> use pesquisa; - entrar dentro do banco </li>
  <li> CREATE TABLE tbl_objeto_pesquisa ( pesquisa_id BIGINT NOT NULL AUTO_INCREMENT, empresa_nome VARCHAR(45) NULL, cnpj VARCHAR(45) NULL, objeto_pesquisa    VARCHAR(45) NULL, tipo_objeto VARCHAR(45) NULL, hora_pesquisa VARCHAR(45) NULL, genero VARCHAR(45) NULL, faixa_etaria VARCHAR(45) NULL, classe_economica VARCHAR(45) NULL, PRIMARY KEY (pesquisa_id)); - criar tabela </li>
  <li> SELECT * FROM tbl_objeto_pesquisa; - visulizar a tabela</li>
  <li> exit - para sair do banco e da imagem</li>
</ul>
  




