import requests
from Datos.conexion_db import insertar_datos, obtener_datos  # Asegúrate de que estas funciones estén definidas en tu archivo de conexión a la DB

def buscar_con_api_serper(query, api_key):
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": api_key
    }
    payload = {
        "q": query
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error al realizar la búsqueda con la API Serper")

def obtener_datos_api_jsonplaceholder():
    url = "https://jsonplaceholder.typicode.com/users"  # Cambia la URL según los datos que necesites
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error al obtener los datos de la API jsonplaceholder")

def almacenar_datos_en_db(datos):
    for dato in datos:
        # Aquí debes definir cómo insertar los datos en tu base de datos
        # Por ejemplo, si son usuarios:
        insertar_datos(dato['id'], dato['name'], dato['username'], dato['email'], dato['phone'])  # Ajusta según tu esquema de DB
    print("Datos almacenados correctamente en la base de datos.")

def consultar_datos_en_db():
    datos = obtener_datos()  # Asegúrate de que esta función esté definida para obtener los datos de la DB
    print("Datos obtenidos de la base de datos:", datos)

def main():
    while True:
        query = input("Ingresa el término de búsqueda para la API SERPER (o escribe 'salir' para volver atrás): ")
        if query.lower() == 'salir':
            print("Volviendo al menú anterior...")
            break  # Salir del bucle y volver atrás

        api_key = "8ae71d320907edfe69633c0f100b59060cf8bc80"
        
        # Paso 1: Buscar en la API SERPER
        try:
            resultados_serper = buscar_con_api_serper(query, api_key)
            print("Resultados de la búsqueda en SERPER:", resultados_serper)
        except Exception as e:
            print(f"Ocurrió un error: {e}")
    # Paso 1: Buscar en la API SERPER
    resultados_serper = buscar_con_api_serper(query, api_key)
    print("Resultados de la búsqueda en SERPER:", resultados_serper)

    # Paso 2: Obtener datos de jsonplaceholder
    datos_jsonplaceholder = obtener_datos_api_jsonplaceholder()
    
    # Paso 3: Almacenar datos en la base de datos
    almacenar_datos_en_db(datos_jsonplaceholder)
    
    # Paso 4: Consultar datos en la base de datos
    consultar_datos_en_db()

if __name__ == "__main__":
    main()