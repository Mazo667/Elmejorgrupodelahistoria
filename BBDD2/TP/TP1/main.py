import psycopg2
import conexion_bdd as con
import ejecutar_consulta as eje
import diccionario_consultas as dic

from psycopg2 import sql

def main():
    connection = con.conexion_bdd()
    if connection:
        print("----------Conexión exitosa a la base de datos.")

        while True:
            print("")
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

            match option:
                case '1':
                    query = dic.consultas['usuarios conectados, IP y consulta']
                    eje.ejecutar_consulta(connection, query)
                case '2':
                    query = dic.consultas['tamaño de base de datos']
                    eje.ejecutar_consulta(connection, query)
                case '3':
                    tabla = input("Introduzca el nombre de la tabla: ")
                    query = dic.consultas['tamaño de una tabla']
                    eje.ejecutar_consulta(connection, query.format(tabla))
                case '4':
                    tabla = input("Introduzca el nombre de la tabla: ")
                    query = dic.consultas['detalles de la tabla']
                    eje.ejecutar_consulta(connection, query.format(tabla))
                case '5':
                    query = dic.consultas['tamaño de las tablas de un esquema']
                    eje.ejecutar_consulta(connection, query)         
                case '6':
                    query = dic.consultas['listado detallado de la bdd']
                    eje.ejecutar_consulta(connection, query)
                case '7':
                    query = input("Introduce la consulta personalizada: ")
                    eje.ejecutar_consulta(connection, query)
        connection.close()
        print("Conexión cerrada.")

if __name__ == '__main__':
    main()
