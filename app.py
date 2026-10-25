import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask import Flask

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/')
def index():
    return render_template ('index.html', Proyecto= 'Mi primer app Flask')


@app.route('/about')
def about():
    return render_template ('about.html', Proyecto= 'Mi primer app Flask')

if __name__== '__main__':
    app.run(debug=True) 

