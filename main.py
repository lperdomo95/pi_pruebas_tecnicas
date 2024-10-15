import os
from sqlalchemy import create_engine
import pandas as pd
import requests
from datetime import datetime as dt


def process_etl():
    # Conectar a la base de datos
    #DB_CONNECTION_STRING = 'mssql+pyodbc://sqlserver:admin2024@34.29.151.224/pi-prueba-tecnica?driver=ODBC+Driver+17+for+SQL+Server'
    try:
        connection_string = os.getenv('DB_CONNECTION_STRING')
        engine = sqlalchemy.create_engine(connection_string)
        print('Conexion exitosa')
    except Exception as e:
        print(f"Error en la conexion: {e}")
    
    # Descargar CSV
    url = "https://strecursoschallenge.blob.core.windows.net/challenge/nuevas_filas.csv?sp=r&st=2024-08-26T20:28:39Z&se=2024-12-31T04:28:39Z&sv=2022-11-02&sr=b&sig=7vZYDdZc7%2B%2FcwVYEAlSCzixAKiSrKlaeU8%2Fns%2B2YQVU%3D"
    response = requests.get(url)
    response.raise_for_status()

    # Procesar CSV a DataFrame
    df = pd.read_csv(pd.io.common.BytesIO(response.content))

    # Transformaciones
    df['fecha_copia'] = dt.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-4] + 'Z'  # Formato YYYY-MM-DDTHH:MM:SS.SS    df = df.drop_duplicates()

    df = df.drop_duplicates()

    # Cargar los datos en la base de datos
    with engine.connect() as conn:
        df.to_sql('Unificado', con=conn, if_exists='append', index=False)

if __name__ == "__main__":
    process_etl()
