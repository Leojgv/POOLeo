import bcrypt

def encriptar_contrasena(contrasena):
    hashed = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
    return hashed