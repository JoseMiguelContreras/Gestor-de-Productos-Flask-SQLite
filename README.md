# Gestión de Productos con Flask y SQLite
Esta aplicación web permite gestionar productos mediante un sistema basado en Flask y una base de datos SQLite. Los usuarios pueden agregar, editar y eliminar productos a través de una interfaz amigable.

# Estructura del proyecto
Aquí tienes una breve descripción de los archivos principales de la aplicación:

# app.py :
Archivo principal que contiene la lógica de la aplicación Flask, define las rutas y la lógica de negocio relacionada con los productos.

# models.py :
Define la clase Producto, que representa un producto en la aplicación y cómo se convierte para ser almacenado en la base de datos.

# templates/index.html :
Archivo HTML que proporciona la interfaz visual para interactuar con la aplicación. Incluye formularios para agregar, editar y listar productos.

# static/styles.css :
Estilos CSS utilizados para dar un diseño atractivo y consistente a la interfaz de usuario.

# base de datos.db :
Base de datos SQLite que almacena los productos.


# Requisitos previos

Antes de configurar y ejecutar la aplicación, asegúrese de tener instalada lo siguiente:

Python 3.12.6 o superior.
Pip (gestor de paquetes de Python).

# Pasos para Configurar el Proyecto

Sigue los siguientes pasos para configurar el proyecto en una nueva máquina Windows.

# 1- Clonar el Proyecto (si es necesario)
Si deseas clonar el proyecto desde un repositorio, usa el siguiente comando (esto es opcional):
git clone <URL_DEL_REPOSITORIO>

# 2-  Crear un entorno virtual
Es recomendable crear un entorno virtual para gestionar las dependencias. Para hacerlo, ejecuta los siguientes comandos en la terminal (cmd o PowerShell) dentro de la carpeta del proyecto:

python -m venv venv

# 3- Activar el Entorno Virtual
Para activar el entorno virtual, use el siguiente comando:
venv\Scripts\activate

Una vez que el entorno virtual esté activo, el nombre del entorno (por ejemplo, venv) aparecerá al principio de la línea de comandos.

# 4-  Instalar las dependencias
Con el entorno virtual activado, instale las dependencias necesarias para que el proyecto funcione correctamente. Ejecuta el siguiente comando:

pip install Flask
pip install Flask-SQLAlchemy

# 5- Configurar la Base de Datos
El proyecto utiliza SQLite para almacenar los productos. No necesitas configurar una base de datos externa, ya que SQLite crea un archivo local llamado database.db.

No es necesario realizar ninguna configuración adicional en cuanto a la base de datos, pero asegúrese de que el archivo database.dbesté en la misma carpeta que los archivos del proyecto.

# 6-  Ejecutar la aplicación
Para iniciar la aplicación, ejecuta el archivo app.pycon el siguiente comando:

python app.py

La aplicación se ejecutará en http://127.0.0.1 : 5000/ . Abra esta URL en su navegador para acceder a la interfaz de usuario.

# 7- Interactuar con la Aplicación
Una vez que la aplicación esté corriendo, podrás:

* Agregar productos : A través del formulario en la página principal.
* Ver productos existentes : La lista de productos aparecerá en la misma página.
* Eliminar productos : Cada producto tendrá un botón para eliminarlo de la base de datos.

# 8-  Detener la aplicación
Cuando desees detener la aplicación, puedes hacerlo presionando Ctrl + C en la terminal donde se está ejecutando el servidor.




# Desarrollado por José Miguel Durán Contreras.
Este proyecto fue desarrollado como una aplicación básica de gestión de productos utilizando Flask y SQLite . Si tienes preguntas o deseas realizar mejoras, no dudes en contactarme.

Este README cubre todos los pasos necesarios para que puedan ejecutar la aplicación en sus máquinas sin problemas, incluyendo la creación y activación del entorno virtual, la instalación de las dependencias necesarias, y cómo ejecutar la aplicación.




