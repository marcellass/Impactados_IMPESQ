from app import app, db, loginManager 
from flask import render_template, make_response
import io



@app.route('/react')
def index():
    
    return render_template('index.html', flask_token= "Meu Token")
