from psycopg2 import sql

def ejecutar_consulta(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        
        if cursor.description:
            # Imprimir encabezados de columna
            column_names = [desc[0] for desc in cursor.description]
            print("\n" + " | ".join(f"{name:<20}" for name in column_names))  # Formato de encabezados
            print("-" * (len(column_names) * 22))  # Línea divisoria
            
            # Imprimir resultados
            results = cursor.fetchall()
            for row in results:
                print(" | ".join(f"{str(value):<20}" for value in row))  # Formato de filas
        else:
            print("Consulta ejecutada correctamente, pero no se devolvieron resultados.")
        
        cursor.close()
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")