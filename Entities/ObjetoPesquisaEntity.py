import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()

def insert(nomeEmpresa, cnpj, objetoPesquisa, tipoObjeto, horapesquisa, faixaEtaria, classeEconomica):
    if nomeEmpresa and cnpj and objetoPesquisa and tipoObjeto and horapesquisa and faixaEtaria and classeEconomica:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into tbl_objeto_pesquisa (empresa_nome, cnpj, objeto_pesquisa, tipo_objeto, hora_pesquisa, faixa_etaria, faixa_etaria) VALUES (%s, %s, %s, %s, %s, %s, %s)', (nomeEmpresa, cnpj, objetoPesquisa, tipoObjeto, horapesquisa, faixaEtaria, classeEconomica))
        conn.commit()

def read():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select empresa_nome, cnpj, objeto_pesquisa, tipo_objeto, hora_pesquisa, faixa_etaria, faixa_etaria from tbl_objeto_pesquisa')
    data = cursor.fetchall()
    conn.commit()
    return data
    
