consultas = {
    'usuarios conectados, IP y consulta':'SELECT username AS Usuario,client_addr AS Cliente IP,query AS Consulta,state AS Estado,query_start AS Consulta inicio tiempo FROM pg_stat_activity;',
    '':''
}