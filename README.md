<h3>Passo a passo para rodar a aplicação: </h3>

git pull - para baixar o projeto do Github atualizado

docker-compose stop - ele para o docker

docker-compose start - starta com as atualizações feitas

docker exec -it <id do container> /bin/bash - entrar dentro da imagem

Dentro da imagem:
mysql -uroot -p - entrar no banco
senha: impactados

create schema pesquisa;

use pesquisa;

CREATE TABLE tbl_objeto_pesquisa ( pesquisa_id BIGINT NOT NULL AUTO_INCREMENT, empresa_nome VARCHAR(45) NULL, cnpj VARCHAR(45) NULL, objeto_pesquisa VARCHAR(45) NULL, tipo_objeto VARCHAR(45) NULL, hora_pesquisa VARCHAR(45) NULL, genero VARCHAR(45) NULL, faixa_etaria VARCHAR(45) NULL, classe_economica VARCHAR(45) NULL, PRIMARY KEY (pesquisa_id));

SELECT * FROM tbl_objeto_pesquisa;

exit - para sair do banco e da imagem

