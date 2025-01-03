import mysql.connector
from prettytable import from_db_cursor
from Auxiliares.constantes import db_user, db_password, db_host, db_database
from Negocio.Managment_Contrasena import decrypt_password
from prettytable import PrettyTable
# Conexion a DB
def conexion_db():
    try:
        cnx = mysql.connector.connect(
            user = db_user,
            password = db_password,
            host = db_host,
            database = db_database)
        return cnx
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None

# Guarda el usuario en la DB
def save_user_DB(userId, name, username, email, phone):
    """Guarda al usuario obtenido en jsonplaceholder en la base de datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "INSERT INTO User (id_user, username, user_email, user_website, user_phone) VALUES (%s,%s,%s,%s,%s);"
        cursor.execute(query, (userId, name, username, email, phone))
        cnx.commit()
        cursor.close()
    print("\nUsuario Guardado en la DB correctamente\n")

# Guarda el Post en la DB
def save_post_DB(id_post, post_title, body_post):
    """Guarda el post obtenido por jsonplaceholder en la base de datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "INSERT INTO Post (id_post, post_title, body_post) VALUES (%s, %s, %s);"
        cursor.execute(query, (id_post, post_title, body_post))
        cnx.commit()
        cursor.close()
        print("\nPost Guardado en la DB correctamente\n")

# Asigna un post a un usuario
def asign_post():
    """Asigna un Post a un usuario que se encuentre en la DB"""

    # Obtiene los datos para asignar
    id_post = int(input("Ingrese el ID del post que desea asignar: "))
    userId = int(input("Ingrese el ID del usuario a asignar: "))

    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "UPDATE Post SET User_id_user = %s WHERE id_post = %s;"
        cursor.execute(query, (userId, id_post))
        cnx.commit()
        cursor.close()
    print("\nEl post se ha asignado correctamente.\n")

# Guarda la Tarea en la DB
def save_todo(id_todo, todo_title, completed):
    """Guarda la Tarea desde Jsonplaceholder en la Base de Datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "INSERT INTO ToDos (id_todo, todo_title, completed) VALUES (%s, %s, %s);"
        cursor.execute(query, (id_todo, todo_title, completed))
        cnx.commit()
        cursor.close()
        print("\nTarea Guardada en la DB correctamente\n")

# Asigna una Tarea a un usuario
def asign_todo():
    """Función para asignar una tarea obtenida desde jsonplaceholder en la base de datos"""
    # Obtener datos
    id_todo = int(input("Ingrese el ID de la tarea que desea asignar: "))
    userId = int(input("Ingrese el ID del usuario a asignar: "))

    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "UPDATE ToDos SET User_id_user = %s WHERE id_todo = %s;"
        cursor.execute(query, (userId, id_todo))
        cnx.commit()
        cursor.close()
        print("\nLa tarea se ha asignado correctamente.\n")

# Ver Tabla de Usuarios
def view_user_DB():
    """Función para ver la tabla de usuarios en la base de datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "SELECT * FROM User;"
        cursor.execute(query)
        try:
            tabla = from_db_cursor(cursor)
            print(tabla)
        except:
            print("\nNo hay usuarios registrados en la DB\n")

# Ver tabla de Posts
def view_post_DB():
    """Función para ver la tabla de posts en la base de datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "SELECT * FROM Post;"
        cursor.execute(query)
        try:
            tabla = from_db_cursor(cursor)
            print(tabla)
        except:
            print("\nNo hay posts registrados en la DB\n")

# Ver tabla de ToDos
def view_todo_DB():
    """Función para ver la tabla de ToDos en la base de datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "SELECT * FROM ToDos;"
        cursor.execute(query)
        try:
            tabla = from_db_cursor(cursor)
            print(tabla)
        except:
            print("\nNo hay ToDos registrados en la DB\n")

def save_encrypted_password(user_id, encrypted_password, encryption_key):
    """Guarda la contraseña encriptada en la base de datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        # Verificar si el user_id existe
        cursor.execute("SELECT id_user FROM User WHERE id_user = %s;", (user_id,))
        if cursor.fetchone() is None:
            print("\nEl usuario ingresado no existe en la DB. No se puede guardar la contraseña.")
            cursor.close()
            return  # Salir de la función si el usuario no existe

        # Si el usuario existe, proceder a guardar la contraseña
        query = "INSERT INTO UserPasswords (user_id, encrypted_password, encryption_key) VALUES (%s, %s, %s);"
        cursor.execute(query, (user_id, encrypted_password, encryption_key))
        cnx.commit()
        cursor.close()
        print("\nContraseña encriptada guardada en la DB correctamente\n")

def get_encrypted_password(user_id):
    """Recupera la contraseña encriptada y la clave de encriptación de la base de datos"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "SELECT encrypted_password, encryption_key FROM UserPasswords WHERE user_id = %s;"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return result
        else:
            print("No se encontró la contraseña para el usuario especificado.")
            return None

def decrypt_password_from_db(user_id):
    """Desencripta la contraseña almacenada en la base de datos y la muestra en el terminal"""
    data = get_encrypted_password(user_id)
    if data:
        encrypted_password, encryption_key = data
        decrypted_password = decrypt_password(encrypted_password.encode(), encryption_key.encode())
        print(f"La contraseña desencriptada para el usuario {user_id} es: {decrypted_password}")

def insertar_datos(userId, name, username, email, phone):
    """Inserta un nuevo usuario en la base de datos."""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = "INSERT INTO User (id_user, name, username, user_email, user_phone) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(query, (userId, name, username, email, phone))
        cnx.commit()
        cursor.close()
        print("Usuario insertado correctamente en la base de datos.")

def obtener_datos():
    """Obtiene todos los usuarios de la base de datos."""
    cnx = conexion_db()
    datos = []
    if cnx:
        cursor = cnx.cursor()
        query = "SELECT * FROM User;"
        cursor.execute(query)
        for (id_user, name, username, user_email, user_phone) in cursor:
            datos.append({
                'id_user': id_user,
                'name': name,
                'username': username,
                'user_email': user_email,
                'user_phone': user_phone
            })
        cursor.close()
    return datos

def guardar_busqueda(query):
    """Guarda la búsqueda en la base de datos y devuelve el ID de la búsqueda."""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query_sql = "INSERT INTO Busqueda (keyword_search) VALUES (%s);"
        cursor.execute(query_sql, (query,))
        cnx.commit()
        busqueda_id = cursor.lastrowid  # Obtiene el ID de la última inserción
        cursor.close()
        return busqueda_id

def guardar_resultado(busqueda_id, titulo, url, descripcion):
    """Guarda un resultado de búsqueda en la base de datos."""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query_sql = "INSERT INTO Resultados (Busqueda_id_search, titulo, url, descripcion) VALUES (%s, %s, %s, %s);"
        cursor.execute(query_sql, (busqueda_id, titulo, url, descripcion))
        cnx.commit()
        cursor.close()

def view_results_search():
    """Muestra los resultados de búsqueda en el terminal"""
    cnx = conexion_db()
    if cnx:
        cursor = cnx.cursor()
        query = """
                    SELECT 
                        b.keyword_search as Busqueda,
                        r.titulo,
                        r.url,
                        r.descripcion
                    FROM 
                        Busqueda b
                    JOIN 
                        Resultados r ON b.id_search = r.Busqueda_id_search;"""
        cursor.execute(query)
        try:
            tabla = from_db_cursor(cursor)
            print(tabla)
        except:
            print("\nNo hay ToDos registrados en la DB\n")