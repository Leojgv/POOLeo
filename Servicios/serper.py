import requests
import json
import Auxiliares.constantes

url = Auxiliares.constantes.URL_SERPER
def menu_serper():
    print("""\n-----------------------------------------------
Menu Serper: """)
    # Solicitar al usuario que ingrese la query
    query = input("Ingrese la query de búsqueda: ")

    payload = json.dumps({
        "q": query  # Usar la query ingresada por el usuario
    })
    headers = {
        'X-API-KEY': Auxiliares.constantes.APIKEY, # Esto tiene que cambiarlo el profe.
        'Content-Type': 'application/json'
    }

    response = requests.post(Auxiliares.constantes.URL_SERPER, headers=headers, data=payload)

    if response.status_code == 200:
        results = response.json()
        print("Resultados de la búsqueda:")
        for result in results.get('organic', []):
            print(f"Título: {result['title']}")
            print(f"URL: {result['link']}")
            print(f"Descripción: {result['snippet']}\n")
        print("\nBusqueda Completada... ")
        print("-----------------------------------------------")
    else:
        print(f"Error: {response.status_code} - {response.text}")