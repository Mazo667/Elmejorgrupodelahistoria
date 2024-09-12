import psycopg2
import conexion_bdd
import ejecutar_consulta
import diccionario_consultas

from psycopg2 import sql

def main():
    connection = conexion_bdd.conexion_bdd()
    if connection:
        print("Conexión exitosa a la base de datos.")
        while True:
            print("-------------------------")
            print("---MENU CONSULTAS---")
            print("1- Obtener los usuarios conectados, IP y consulta.")
            print("2- Obtener el tamaño de la base de datos del servidor.")
            print("3- Obtener el tamaño de una tabla.")
            print("4- Obtener detalles de las tablas. orden de los campos, nombre y tipo de dato.")
            print("5- Obtener el tamaño de las tablas de un esquema.")
            print("6- Listado por BBDD del tamaño total de la BBDD, el nombre del esquema, el nombre de la tabla, el tamaño  total de la tabla, el tamaño de la tabla y el tamaño del índice")
            print("7- Consulta personalizada.")
            
            option = input("Escribe la opcion: (o 'salir' para terminar): ")
            if option.lower() == 'salir':
                break
            #ejecutar_consulta(connection, query)
            match option:
                case '1':
                    query = diccionario_consultas.consultas['usuarios conectados, IP y consulta']
                    ejecutar_consulta.ejecutar_consulta(connection, query)
        connection.close()
        print("Conexión cerrada.")

if __name__ == '__main__':
    main()
