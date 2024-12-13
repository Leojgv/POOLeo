from Datos import data_empleados
import Negocio.encriptacion
from Negocio.negocio_empleados import listado_empleados as listado
import Negocio.negocio_usuarios
import Negocio.generacion_clave

# data = listado()
# print(data)

Negocio.generacion_clave.generacion_clave()
# contrasena = input("Ingrese Contraseña:")
# contrasena_encriptada = ''
# contrasena_encriptada = negocio.encriptacion.encriptar_contrasena(contrasena)

# contrasena = input("Ingrese Contraseña:")
# contrasena_anterior = negocio.encriptacion.desencriptar_contrasena(contrasena_encriptada)
# if contrasena_anterior == contrasena:
#     pass