<h2>Passo a passo para utilização: </h2>

<h3>Sprint 1 </h3>

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
  <li> CREATE TABLE tbl_objeto_pesquisa ( pesquisa_id BIGINT NOT NULL AUTO_INCREMENT, empresa_nome VARCHAR(45) NULL, cnpj VARCHAR(45) NULL, objeto_pesquisa    VARCHAR(45) NULL, tipo_objeto VARCHAR(45) NULL, hora_pesquisa VARCHAR(45) NULL, genero VARCHAR(45) NULL, faixa_etaria VARCHAR(45) NULL, classe_economica VARCHAR(45) NULL, PRIMARY KEY (pesquisa_id)); - criação da tabela </li>
  <li> SELECT * FROM tbl_objeto_pesquisa; - visulização da tabela</li>
  <li> exit - para sair do banco e da imagem</li>
</ul>
 
 <h3>Sprint 2 </h3>
 
 <h4>Fora da imagem/No dockerplay</h4>
<ul>
  <li> docker-compose down --rmi all - da um down no container e remove todas as imagens</li> 
</ul>

 <h4>Dentro da imagem</h4>
<ul>
  <li> CREATE TABLE tbl_cadastro_convidado ( convidado_id BIGINT NOT NULL AUTO_INCREMENT, nomeConvidado VARCHAR(50) NULL, sobrenomeConvidado VARCHAR(50) NULL, datanasc VARCHAR(50) NULL, rgConvidado VARCHAR(50) NULL, ufConvidado VARCHAR(50) NULL, cpfConvidado VARCHAR(50) NULL, enderecoConvidado VARCHAR(50) NULL, bairroConvidado VARCHAR(50) NULL, cidadeConvidado VARCHAR(50) NULL, cepConvidado VARCHAR(50) NULL, zonaConvidado VARCHAR(50) NULL, formacaoConvidado VARCHAR(50) NULL, escolaridadeConvidado VARCHAR(50) NULL, ano_escolaridade VARCHAR(50) NULL, periodoConvidado VARCHAR(50) NULL, estadoCivilConvidado VARCHAR(50) NULL, filhoConvidado VARCHAR(50) NULL, primeiroFilho VARCHAR(50) NULL, segundoFilho VARCHAR(50) NULL, nascimentoPrimeiroFilho VARCHAR(50) NULL, nascimentoSegundoFilho VARCHAR(50) NULL, trabalhoConvidado VARCHAR(50) NULL, horarioTrabalho VARCHAR(50) NULL, empresaConvidado VARCHAR(50) NULL, ramoConvidado VARCHAR(50) NULL, telefoneEmpresa VARCHAR(50) NULL, telefoneResidencial VARCHAR(50) NULL, celularConvidado VARCHAR(50) NULL, operadoraConvidado VARCHAR(50) NULL, opcaoOperadora VARCHAR(50) NULL, emailConvidado VARCHAR(50) NULL, pesquisaMercado VARCHAR(50) NULL, mktPubli VARCHAR(50) NULL, rjrTv VARCHAR(50) NULL, participouPesquisa VARCHAR(50) NULL, tipoPesquisa VARCHAR(50) NULL, dataUltimaPesquisa VARCHAR (50) NULL, assuntoUltimaPesquisa VARCHAR (50) NULL, classificacao VARCHAR(45) NULL, PRIMARY KEY (convidado_id)); - criação da tabela </li>
</ul>
