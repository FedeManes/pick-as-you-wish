from flask import request, make_response, redirect, render_template
from app import create_app
from app.model import db, Aventura, crear_datos_iniciales
from dotenv import load_dotenv

load_dotenv()
app = create_app()

with app.app_context():
    db.init_app(app)
    db.create_all()
    print("Base de datos creada")
    crear_datos_iniciales() 
    print("Datos Iniciales creados")

@app.errorhandler(404)
def not_found(error):
        return render_template('404.html',error=error)
    
@app.route('/')
def index():
    response =  make_response(redirect('/start'))
    return response
    
@app.route('/start')
def start():
    start = Aventura.query.filter_by(id=1).first()
    context = {
        'story': start.descripcion,
        'chooseText': start.opcionesText,
        'choose': start.opciones
    }
    return render_template('start.html', **context)

@app.route('/choose', methods=['POST'])
def choose():
    option = request.form.get('option')
    optionChosen = Aventura.query.filter_by(id=option).first()
    context = {
        'id': optionChosen.id,
        'story': optionChosen.descripcion,
        'chooseText': optionChosen.opcionesText,
        'choose': optionChosen.opciones
    }
    return render_template('choose.html', **context)