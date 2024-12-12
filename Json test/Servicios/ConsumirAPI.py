import requests
from Clases.Post import Post
import Auxiliares.Variables_fijas 

def leer_post_por_id(post_id):
    """Función para leer un post desde JSON Placeholder según el id"""
    try:
        ans = requests.get(f"{Auxiliares.Variables_fijas.URL_Post}/{post_id}")
        ans.raise_for_status()  # Lanza un error si la respuesta no es 200
        post_data = ans.json()
        
        # Crear una instancia de Post y asignar los valores
        post = Post()
        post.userId = post_data['userId']
        post.id = post_data['id']
        post.title = post_data['title']
        post.body = post_data['body']
        
        return post
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print("El post no fue encontrado.")