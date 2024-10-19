from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesion'

usuarios = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        
        for u in usuarios:
            if u['usuario'] == usuario and u['password'] == password:
                session['usuario'] = u['usuario']
                session['nombre'] = u['nombre']
                return redirect(url_for('salida'))
        
        flash('Usuario o contraseña incorrectos')
        return redirect(url_for('index'))
    
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        usuario = request.form['usuario']
        password = request.form['password']
        
        usuarios.append({
            'nombre': nombre,
            'email': email,
            'telefono': telefono,
            'usuario': usuario,
            'password': password
        })
        
        flash('Registro exitoso. Por favor, inicia sesión.')
        return redirect(url_for('index'))
    
    return render_template('registro.html')

@app.route('/salida')
def salida():
    
    if 'usuario' in session:
        nombre = session['nombre']
        return render_template('salida.html', nombre=nombre)
    
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    session.pop('nombre', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
