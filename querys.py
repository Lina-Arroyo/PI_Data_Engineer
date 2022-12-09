import pandas as pd

def Query1(con, anio, plataf):
    query = f"SELECT title, time_of FROM datos WHERE time_of = (SELECT MAX(time_of) FROM datos WHERE release_year = '{anio}' and plataforma = '{plataf}') and min_season = 'min' and release_year = '{anio}' and plataforma = '{plataf}'"
    df = pd.read_sql(query, con)
    return df

def Query2(con, plataf):
    query = f"SELECT count(plataforma) AS plataforma, type FROM plataformas_stream WHERE plataforma = '{plataf}' GROUP BY plataforma, type"
    df =pd.read_sql(query, con)
    return df

def Query3(con, genero):
    query = f"SELECT COUNT(listed_in) AS cantidad, plataforma FROM plataformas_stream WHERE listed_in LIKE %'{genero}'% and plataforma = 'amazon' GROUP BY plataforma "
    df =pd.read_sql(query, con)
    return df 

def Query4(con, año, plataforma):
    query = f"SELECT COUNT(cast) as cantidad, cast, plataforma FROM plataformas_stream WHERE cast LIKE %'andrea libman'% and release_year = '{año}' and plataformas = '{plataforma}' group by plataforma"
    df =pd.read_sql(query, con)
    return df 