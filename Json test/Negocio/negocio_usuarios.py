"""from modelos.usuario import Usuario as usuario
from negocio.encriptacion import encriptar_contrasena as encriptar, desencriptar_contrasena as desencriptar
import datos.data_usuarios

contrasena_encriptada = ''

def buscar_usuario(busqueda):
    data = datos.data_usuarios.buscar_usuario(busqueda)
    usuario_login = usuario()
    for registro in data:
        usuario_login.rut_empleado = registro[0]
        usuario_login.correo_empleado = registro[1]
        usuario_login.contrasena_empleado = registro[2]
        usuario_login.permisos_rol = registro[3]
        contrasena_guardada = desencriptacion_contrasena(registro[2])

def encriptacion_contrasena(contrasena):
    contrasena_encriptada = encriptar(contrasena)
    print(contrasena_encriptada)

def desencriptacion_contrasena(contrasena):
    resultado = desencriptar(contrasena, contrasena_encriptada)
    print(resultado)"""