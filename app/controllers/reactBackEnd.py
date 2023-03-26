from app import app, db, loginManager
from flask import render_template, flash, redirect, url_for, request, send_from_directory


@app.route('/react')
def index():
    return render_template('index.html', flask_token= "Meu Token")