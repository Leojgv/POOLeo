import Servicios.InteractAPI, Datos.conexion_db, Servicios.Managment_Contrasena
import Datos.conexion_db
from Servicios.Servicio_serper import main as Servicio_serper
import Servicios.Servicio_serper
# Menú de jsonplaceholder
def menu_json():
    """Menú interactivo para utilizar las funciones en jsonplaceholder"""
    while True:
        print(""" 
Menú JsonPlaceholder:
1. Consultar Datos de Usuario
2. Consultar Post
3. Consultar Tarea
0. Salir de este menú
""")
        try: 
            option = int(input("Ingrese una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número")
            continue  # Volver al inicio del bucle

        # User
        if option == 1:
            user = Servicios.InteractAPI.view_user()
            if user:
                answer = input("\n¿Desea Guardar el Usuario en la Base de Datos? (si/no): ")
                if answer == 'si':
                    Datos.conexion_db.save_user_DB(user.userId, user.name, user.username, user.email, user.phone)
                elif answer == 'no':
                    print("\nEl Usuario no se ha guardado en la DB\n")
                    continue

        # Post
        elif option == 2:
            post = Servicios.InteractAPI.read_post()
            if post:
                answer = input("\n¿Desea Guardar el post en la Base de Datos? (si/no): ")
                if answer == 'si':
                    Datos.conexion_db.save_post_DB(post.id, post.title, post.body)
                elif answer == 'no':
                    print("\nEl Post no se ha guardado en la DB\n")
                    continue

        # Tarea
        elif option == 3:
            todo = Servicios.InteractAPI.view_todos()
            if todo:
                answer = input("\n¿Desea Guardar la Tarea en la Base de Datos? (si/no): ")
                if answer == 'si':
                    Datos.conexion_db.save_todo(todo.Id, todo.title, todo.completed)
                elif answer == 'no':
                    print("\nLa Tarea no se ha guardado en la DB\n")

        #Salir
        elif option == 0:
            print("Volviendo al menú principal...")
            break

def menu_db():
    """Menú interacctivo para utilizar las funciones de la DB"""
    while True:
        print("""
Menú Base de Datos:
1. Mostrar Usuarios
2. Mostrar Posts
3. Mostrar Tareas
4. Asignar Post a un Usuario
5. Asignar Tarea a un Usuario
6. Desencriptar Contraseña
0. Salir de este menú
""")
        try:
            option = int(input("Ingrese una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número")
            return

        # Ver Users
        if option == 1:
            Datos.conexion_db.view_user_DB()
            continue
        # Ver Posts
        elif option == 2:
            Datos.conexion_db.view_post_DB()
            continue
        # Ver Tareas
        elif option == 3:
            Datos.conexion_db.view_todo_DB()
            continue
        # Asignar Post
        elif option == 4:
            Datos.conexion_db.asign_post()
            continue
        # Asignar Tarea
        elif option == 5:
            Datos.conexion_db.asign_todo()
            continue
        elif option == 6:
            user_id = input("Ingrese el ID del usuario para desencriptar: ")
            Datos.conexion_db.decrypt_password_from_db(user_id)
        elif option == 0:
            print("Volviendo al Menú principal...")
            break

#Menu Principal 
def mostrar_menu_principal():
    """Muestra el menú principal y devuelve la opción seleccionada."""
    print("""
Menú del Programa:
1. Menú JsonPlaceholder.
2. Menú Base de Datos. 
3. Encriptacion.
4. Serper.
0. Salir""")
    return int(input("Ingrese una opción: "))

def ejecutar_opcion(opcion):
    """Ejecuta la opción seleccionada del menú."""
    if opcion == 1:
        menu_json()
    elif opcion == 2:
        menu_db()
    elif opcion == 3:
        Servicios.Managment_Contrasena.password_management()
    elif opcion == 4:
        Servicios.Servicio_serper.main()
    elif opcion == 0:
        print("Saliendo del programa...")
        return False
    return True

def main():
    """Función principal que ejecuta el programa."""
    continuar = True
    while continuar:
        opcion = mostrar_menu_principal()
        continuar = ejecutar_opcion(opcion)

if __name__ == "__main__":
    main()