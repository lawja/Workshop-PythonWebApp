from flask import url_for, redirect, render_template, session
from app import app

@app.route('/')
def index():
	return render_template('index.html')