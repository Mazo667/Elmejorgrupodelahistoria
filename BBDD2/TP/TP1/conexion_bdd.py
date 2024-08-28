import psycopg2
from psycopg2 import sql

def conexion_bdd():
    try:
        connection = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='admin',
            host='localhost',
            port='5432'
        )
        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None