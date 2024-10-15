import pandas as pd
from datetime import datetime

df_semanal = pd.read_csv('/Users/lucasperdomo/Library/Mobile Documents/com~apple~CloudDocs/Documents/Lucas/Proyectos/prueba_tecnica/pi_data/bajadas/nuevas_lineas_20241010.csv',delimiter=',')

df_semanal['fecha_copia'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-4] + 'Z'  # Formato YYYY-MM-DDTHH:MM:SS.SS

df_semanal = df_semanal.drop_duplicates()

print(df_semanal.head())

