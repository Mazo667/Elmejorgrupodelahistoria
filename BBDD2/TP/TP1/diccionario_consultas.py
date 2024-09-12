consultas = {
    'usuarios conectados, IP y consulta':'SELECT username AS Usuario,client_addr AS Cliente_iP,query AS Consulta,state AS Estado,query_start AS Consulta_inicio_tiempo FROM pg_stat_activity;',
    '':''
}