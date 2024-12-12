import os
from cryptography.fernet import Fernet

def generacion_clave():
    key = Fernet.generate_key()
    clave_guardar = f"clave_guardada = {key}"
    
    
    file = 'clave.py'
    location = os.path.join('auxiliares', file)
    location = os.path.abspath(location)
    location = os.path.realpath(location)    
    archivo = open(f"{location}", "w+")
    archivo.write(clave_guardar)
    archivo.close()