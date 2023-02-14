import pandas as pd
import Conexion as conexion

conn = conexion.get_db()
cursor = conn.cursor()

def Query1(anio, plataf):
    query = f"SELECT title, time_of FROM plataformas_stream WHERE time_of = (SELECT MAX(time_of) FROM plataformas_stream WHERE release_year = '{anio}' and plataforma = '{plataf}') and min_season = 'min' and release_year = '{anio}' and plataforma = '{plataf}'"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def Query2(plataf):
    query = f"SELECT count(plataforma) AS plataforma, type FROM plataformas_stream WHERE plataforma = '{plataf}' GROUP BY plataforma, type"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def Query3(genero):
    query = f"SELECT COUNT(listed_in) AS cantidad, plataforma FROM plataformas_stream WHERE listed_in LIKE '%{genero}%' GROUP BY plataforma "
    cursor.execute(query)
    result = cursor.fetchall()
    return result 

def Query4(año, plataforma):
    query = f"SELECT COUNT(cast) as cantidad, cast, plataforma FROM plataformas_stream WHERE cast LIKE '%andrea libman%' and release_year = '{año}' and plataforma = '{plataforma}' group by plataforma"
    cursor.execute(query)
    result = cursor.fetchall()
    return result