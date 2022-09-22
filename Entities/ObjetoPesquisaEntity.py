import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()

def insert(nomeEmpresa, cnpj, objetoPesquisa, tipoObjeto, horapesquisa, faixaEtaria, classeEconomica):
    if nomeEmpresa and cnpj and objetoPesquisa and tipoObjeto and horapesquisa and faixaEtaria and classeEconomica:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into tbl_objeto_pesquisa (empresa_nome, empresa_cnpj, empresa_objeto_pesquisa, empresa_tipo_objeto, empresa_hora_pesquisa, empresa_faixa_etaria, empresa_faixa_etaria) VALUES (%s, %s, %s)', (nome, cpf, endereco))
        conn.commit()

def read():
    
