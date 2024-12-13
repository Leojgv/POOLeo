import Datos.conexion_db as conexion

def listado_empleados():
    consulta = f"""
        SELECT 
            E.id_empleado,
            E.rut_empleado,
            E.nombre_empleado,
            DATE_FORMAT(E.fecha_contrato, '%d/%m/%Y'),
            CONCAT('$', FORMAT(E.salario_empleado, 2)),
            E.correo_empleado,
            E.telefono_empleado,
            DATE_FORMAT(E.fecha_nacimiento_empleado, '%d/%m/%Y'),
            E.id_tipo_empleado,
            E.id_rol,
            E.codigo_pais
        FROM empleados E
        WHERE E.habilitado = 1;
        """
    data = conexion.leer_datos(consulta)
    return data

def buscar_empleado(busqueda):
        consulta = f"""
            SELECT 
                E.id_empleado,
                E.rut_empleado,
                E.nombre_empleado,
                DATE_FORMAT(E.fecha_contrato, '%d/%m/%Y'),
                CONCAT('$', FORMAT(E.salario_empleado, 2)),
                E.correo_empleado,
                E.telefono_empleado,
                DATE_FORMAT(E.fecha_nacimiento_empleado, '%d/%m/%Y'),
                E.id_tipo_empleado,
                E.id_rol,
                E.codigo_pais
                IF(E.habilitado = 1, 'True', 'False')
            FROM empleados E
            JOIN tipos_empleado TE ON E.id_tipo_empleado = TE.id_tipo_empleado
            JOIN roles R ON E.id_rol = R.id_rol
            JOIN paises P ON E.codigo_pais = P.codigo_pais
            WHERE E.rut_empleado LIKE '%{busqueda}%'
                OR E.nombre_empleado LIKE '%{busqueda}%'
                OR E.correo_empleado LIKE '%{busqueda}%';
            """
        data = conexion.leer_datos(consulta)   
        return data