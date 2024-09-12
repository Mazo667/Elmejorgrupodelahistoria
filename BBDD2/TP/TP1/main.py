import psycopg2
import conexion_bdd
import ejecutar_consulta
from psycopg2 import sql

def main():
    connection = conexion_bdd()
    if connection:
        print("Conexión exitosa a la base de datos.")
        while True:
            print("-------------------------")
            print("---MENU CONSULTAS---")
            print("1- Obtener todas las bases de datos disponibles")
            print("2- Obtener los Roles que se puede conectar al servidor")
            print("3- ")
            
            query = input("Escribe tu consulta SQL (o 'salir' para terminar): ")
            if query.lower() == 'salir':
                break
            ejecutar_consulta(connection, query)
        connection.close()
        print("Conexión cerrada.")

if __name__ == '__main__':
    main()
    