consultas = {
    'usuarios conectados, IP y consulta':"SELECT pg_stat_activity.usename AS Usuario,client_addr AS Cliente_iP,query AS Consulta,state AS Estado,query_start AS Consulta_inicio_tiempo FROM pg_stat_activity;",
    'tamaño de base de datos':"SELECT datname, pg_size_pretty(pg_database_size(datname)) from pg_database;",
    'tamaño de una tabla':"SELECT pg_size_pretty(pg_total_relation_size('{}'));",
    'tamaño de las tablas de un esquema':"SELECT c.relname tabla, pg_size_pretty(pg_total_relation_size(c.oid)) tamanio_total FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace WHERE c.relkind = 'r' AND n.nspname = 'public' ORDER BY pg_total_relation_size(c.oid) DESC;",
    'detalles de la tabla':"SELECT column_name nombre_columna, ordinal_position posicion, data_type tipo_dato, is_nullable es_nulo, character_maximum_length longitud_maxima FROM information_schema.columns WHERE table_name = '{}' ORDER BY ordinal_position;",
    'listado detallado de la bdd':"SELECT pg_database.datname, pg_namespace.nspname, pg_class.relname, pg_size_pretty(pg_total_relation_size(pg_class.oid)), pg_size_pretty(pg_table_size(pg_class.oid)), pg_size_pretty(pg_indexes_size (pg_class.oid)) from pg_class join pg_namespace on pg_class.relnamespace = pg_namespace.oid join pg_database on pg_database.datname = current_database() where pg_class.relkind= 'r';"
}

