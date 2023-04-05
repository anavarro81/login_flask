from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from flask_mysqldb import MySQL

# Models:
from models.modelUser import ModelUser

# Entities:
from models.entities.User import User

app=Flask(__name__)

# Crea la conexion con la bbdd. 
# Se crea una instancia de MySQL que recibe como parametro la aplicación (app)

db = MySQL(app)


@app.route('/')
def index():
# Si entra por la raiz, redirecciona a login.     
    return redirect (url_for('login'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    
    

    # Se envia el formulario (mÉtodo = 'POST')
    if request.method == "POST":
        
        # Crea un usuario con el nombre y la password indicados. 
        user = User(0, request.form['usuario'], request.form['password'])
        
        # Comprueba en BBDD si existe el usaurio. 
        logged_user = ModelUser.login(db, user)

        print (f'logged_user ==> {logged_user}')
        
        # Si existe en usuario
        if logged_user != None:
            # Si la password es True si la hemos encontrado en la BBDD. 
            if logged_user.password:
                # Redirecciona a la pagina de bienvenida 'home.html'
                return redirect (url_for('home'))
            else:
                # El password no coincide. 
                flash('Contraseña incorrecta..')
                return render_template('auth/login.html')
        else:
            # Muestra mensaje de error. 
            flash('Usuario no encontrado...')
            return render_template('auth/login.html')
    else:
    # Se muestra el formulario por primera vez (método = 'GET')
        return render_template('auth/login.html')

@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()





