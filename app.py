from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import base_de_datos as bdd
import sqlite3

app = Flask(__name__)
app.secret_key = '09112017poiuy'  # Cambia esto en producción

def crear_tablas():
    conexion = bdd.conexionBD()
    cursor = conexion.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            apellido TEXT NOT NULL,
            gmail TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    
    conexion.commit()
    conexion.close()

@app.route('/')
def inicio():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    conexion = bdd.conexionBD()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productosRecibidos = cursor.fetchall()
    conexion.close()
    
    return render_template('index.html', productos=productosRecibidos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conexion = bdd.conexionBD()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conexion.close()

        if user:
            session['username'] = user['username']
            return redirect(url_for('inicio'))
        else:
            # Enviar mensaje de error al template si las credenciales son incorrectas
            return render_template('login.html', error='Nombre de usuario o contraseña incorrectos.')
    
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        apellido = request.form['apellido']
        gmail = request.form['gmail']
        password = request.form['password']

        conexion = bdd.conexionBD()
        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (username, apellido, gmail, password) VALUES (?, ?, ?, ?)", 
                           (username, apellido, gmail, password))
            conexion.commit()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            # Si el nombre de usuario o correo ya están en uso, mostrar un mensaje de error
            return render_template('registro.html', error="El nombre de usuario o Gmail ya están en uso.")
        except Exception as e:
            # Para cualquier otro tipo de error
            return render_template('registro.html', error="Ocurrió un error en el registro.")
        finally:
            conexion.close()
    
    return render_template('registro.html')

@app.route('/productos', methods=['POST'])
def agregarProducto():
    if 'username' not in session:
        return redirect(url_for('login'))

    nombre = request.form['name']
    precio = request.form['price']
    cantidad = request.form['quantity']
    id_producto = request.form.get('id_producto')  # Obtener el ID del producto si existe

    conexion = bdd.conexionBD()
    cursor = conexion.cursor()
    
    if nombre and precio and cantidad:
        if id_producto:  # Si id_producto existe, estamos editando
            query = "UPDATE productos SET name = ?, price = ?, quantity = ? WHERE id = ?"
            cursor.execute(query, (nombre, precio, cantidad, id_producto))
        else:  # Nuevo producto
            query = "INSERT INTO productos (name, price, quantity) VALUES (?, ?, ?)"
            cursor.execute(query, (nombre, precio, cantidad))
        
        conexion.commit()
    conexion.close()
    return redirect(url_for('inicio'))

@app.route('/eliminar/<int:id_producto>')
def eliminar(id_producto):
    if 'username' not in session:
        return redirect(url_for('login'))

    conexion = bdd.conexionBD()
    cursor = conexion.cursor()
    query = "DELETE FROM productos WHERE id = ?"
    cursor.execute(query, (id_producto,))
    conexion.commit()
    conexion.close()
    return redirect(url_for('inicio'))

@app.route('/cargar/<int:id_producto>')
def cargarProducto(id_producto):
    if 'username' not in session:
        return redirect(url_for('login'))

    conexion = bdd.conexionBD()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()

    # Obtener todos los productos para renderizar en la vista
    cursor.execute("SELECT * FROM productos")
    productosRecibidos = cursor.fetchall()
    conexion.close()

    return render_template('index.html', productos=productosRecibidos, producto=producto)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.errorhandler(404)
def notFound(error=None):
    mensaje = {
        'mensaje': 'No encontrado ' + request.url,
        'estado': '404 No Encontrado'
    }
    response = jsonify(mensaje)
    response.status_code = 404
    return response

if __name__ == '__main__':
    crear_tablas()
    app.run(debug=True)
