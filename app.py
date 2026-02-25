from flask import Flask, render_template
from config import Config
from models import db
import os

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Crear base de datos automáticamente
with app.app_context():
    if not os.path.exists('instance'):
        os.makedirs('instance')
    db.create_all()


@app.route('/')
def inicio():
    return render_template('inicio.html')


if __name__ == '__main__':
    app.run(debug=True)