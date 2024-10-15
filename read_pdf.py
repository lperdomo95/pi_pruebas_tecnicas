"""import requests

# URL del archivo que deseas descargar
url = "https://strecursoschallenge.blob.core.windows.net/challenge/nuevas_filas.csv?sp=r&st=2024-08-26T20:28:39Z&se=2024-12-31T04:28:39Z&sv=2022-11-02&sr=b&sig=7vZYDdZc7%2B%2FcwVYEAlSCzixAKiSrKlaeU8%2Fns%2B2YQVU%3D"


file_name = 'nuevas_lineas_20241010.csv'  # Reemplaza con el nombre deseado

with requests.get(url) as r:
    # Nombre con el que quiero descargar el archivo.
    with open(file_name, "wb") as f:
        f.write(r.content)
"""

import requests
from datetime import datetime
import os

def download_csv(url, file_name):
    try:
        # Realiza la solicitud para descargar el archivo
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error si la solicitud falló

        # Escribe el contenido del archivo CSV en un nuevo archivo
        with open(file_name, "wb") as f:
            f.write(response.content)
        print(f"Archivo {file_name} descargado exitosamente.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el archivo: {e}")

# URL del archivo que deseas descargar
url = "https://strecursoschallenge.blob.core.windows.net/challenge/nuevas_filas.csv?sp=r&st=2024-08-26T20:28:39Z&se=2024-12-31T04:28:39Z&sv=2022-11-02&sr=b&sig=7vZYDdZc7%2B%2FcwVYEAlSCzixAKiSrKlaeU8%2Fns%2B2YQVU%3D"

# Crea la carpeta "bajadas" si no existe
output_dir = "bajadas"
os.makedirs(output_dir, exist_ok=True)

# Genera un nombre de archivo basado en la fecha actual
file_name = os.path.join(output_dir, f'nuevas_lineas_{datetime.now().strftime("%Y%m%d")}.csv')  # Formato: bajadas/nuevas_lineas_20241010.csv

# Llama a la función para descargar el archivo
download_csv(url, file_name)
