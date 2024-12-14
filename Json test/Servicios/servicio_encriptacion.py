from cryptography.fernet import Fernet

def generar_key():
    """Genera una clave para la encriptación."""
    return Fernet.generate_key()

def encriptar_contrasena(contrasena, key):
    """Encripta la contraseña utilizando Fernet."""
    fernet = Fernet(key)
    contrasena_encriptada = fernet.encrypt(contrasena.encode())
    return contrasena_encriptada

def desencriptar_contrasena(contrasena_encriptada, key):
    """Desencripta la contraseña utilizando Fernet."""
    fernet = Fernet(key)
    contrasena_desencriptada = fernet.decrypt(contrasena_encriptada).decode()
    return contrasena_desencriptada

def Main():
    # Generar una clave
    key = generar_key()
    print(f"Clave generada: {key.decode()}")

    # Solicitar la contraseña al usuario
    contrasena = input("Ingresa la contraseña a encriptar: ")
    
    # Encriptar la contraseña
    contrasena_encriptada = encriptar_contrasena(contrasena, key)
    print(f"Contraseña encriptada: {contrasena_encriptada.decode()}")

    # Desencriptar la contraseña
    contrasena_desencriptada = desencriptar_contrasena(contrasena_encriptada, key)
    print(f"Contraseña desencriptada: {contrasena_desencriptada}")

    # Comparar la contraseña original con la desencriptada
    if contrasena == contrasena_desencriptada:
        print("La contraseña coincide.")
    else:
        print("La contraseña no coincide.")

if __name__ == "__main__":
    Main()