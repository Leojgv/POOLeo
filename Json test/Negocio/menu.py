import Servicios.ConsumirAPI

def menu():
    """Menú interactivo para utilizar las funciones"""
    while True:
        print(""" 
Menú de JSONplaceholder
1. Consultar Post
2. Salir
""")
        try: 
            option = int(input("Ingrese una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número")
            continue  # Volver al inicio del bucle
        
        if option == 1:
            post_id = int(input("Ingrese el ID del post que desea leer: "))
            post = Servicios.ConsumirAPI.leer_post_por_id(post_id)
            if post:
                print(f"\nPost ID: {post.id}\nUserID: {post.userId}\nTítulo: {post.title}\nCuerpo: {post.body}")
        
        elif option == 2:
            print("Saliendo del programa...")
            break