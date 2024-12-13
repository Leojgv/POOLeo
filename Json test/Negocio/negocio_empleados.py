from Modelos.empleado import Empleado as empleado
from Modelos.tipo_empleado import TipoEmpleado as tipo_empleado
from Modelos.rol import Rol as rol
from Modelos.pais import Pais as pais
import Datos.data_empleados
import Datos.data_tipo_empleado
import Datos.data_rol
import Datos.data_paises

def listado_empleados():    
    lista_empleados = []
    data = Datos.data_empleados.listado_empleados()
    for registro in data:
        nuevo_empleado = empleado()
        nuevo_empleado.id_empleado = registro[0]
        nuevo_empleado.rut_empleado = registro[1]
        nuevo_empleado.nombre_empleado = registro[2]
        nuevo_empleado.fecha_contrato = registro[3]
        nuevo_empleado.salario_empleado = registro[4]
        nuevo_empleado.correo_empleado = registro[5]
        nuevo_empleado.telefono_empleado = registro[6]
        nuevo_empleado.fecha_nacimiento_empleado = registro[7]
        
        data_tipo_empleado = Datos.data_tipo_empleado.buscar_tipo_empleado_por_id(registro[8])
        for registro_tipo_empleado in data_tipo_empleado:
            nuevo_tipo_empleado = tipo_empleado()
            nuevo_tipo_empleado.id_tipo_empleado = registro_tipo_empleado[0]
            nuevo_tipo_empleado.tipo_empleado = registro_tipo_empleado[1]
            nuevo_tipo_empleado.descripcion_tipo_empleado = registro_tipo_empleado[2]
        
        data_rol_empleado = Datos.data_rol.buscar_rol_por_id(registro[9])
        for registro_rol in data_rol_empleado:
            nuevo_rol = rol()
            nuevo_rol.id_rol = registro_rol[0]
            nuevo_rol.rol = registro_rol[1]
            nuevo_rol.descripcion_rol = registro_rol[2]
            nuevo_rol.permisos_rol = registro_rol[3]
        
        data_pais = Datos.data_paises.buscar_pais(registro[10])
        for registro_pais in data_pais:
            nuevo_pais = pais()
            nuevo_pais.codigo_pais = registro_pais[0]
            nuevo_pais.codigo_iso3_pais = registro_pais[1]
            nuevo_pais.nombre_pais = registro_pais[2]
            nuevo_pais.gentilicio_pais = registro_pais[3]
        
        lista_empleados.append(nuevo_empleado)    
    return lista_empleados