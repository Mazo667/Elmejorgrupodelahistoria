from psycopg2 import sql

def ejecutar_consulta(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        if cursor.description:  # Verifica si la consulta devuelve resultados
            results = cursor.fetchall()
            for row in results:
                print(row)
        else:
            print("Consulta ejecutada correctamente.")
        cursor.close()
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")