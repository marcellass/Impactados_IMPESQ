import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL


def insert(nomeEmpresa, cnpj, objetoPesquisa, tipoObjeto, horapesquisa, idade, classeEconomica):
    if nomeEmpresa and cnpj and objetoPesquisa and tipoObjeto and horapesquisa and idade and classeEconomica:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into tbl_user (user_name, user_cpf, user_endereco) VALUES (%s, %s, %s)', (nome, cpf, endereco))
        conn.commit()
