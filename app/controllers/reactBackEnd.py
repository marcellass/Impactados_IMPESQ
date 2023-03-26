from app import app, db, loginManager, react
from flask import render_template, flash, redirect, url_for, request, send_from_directory


@app.route('/react')
def index():
    return react.render('index.html')