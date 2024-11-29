import sqlite3

def conexionBD():
    try:
        # Cambia 'productos.db' por el nombre de tu base de datos si es necesario
        conexion = sqlite3.connect('productos.db')
        conexion.row_factory = sqlite3.Row  # Permitir acceso por nombre de columna
        print('Conexión exitosa a SQLite')
        return conexion
    except sqlite3.Error as e:
        print(f'Error de conexión: {e}')
        return None
