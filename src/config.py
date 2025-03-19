import os

# Definir la ruta de la base de datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Directorio base del proyecto
DATABASE_PATH = os.path.join(BASE_DIR, "db", "JM.sqlite")