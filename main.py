#Fase 5
import os
import mysql.connector
from fastapi import FastAPI
from starlette.responses import RedirectResponse
import querys as consultas
import Conexion as conexion

app = FastAPI(title="API consultas PI data engineer")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/dbtest")
def dbtest():
    conn = conexion.get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT plataforma FROM plataformas_stream GROUP BY plataforma")
    result = cursor.fetchall()
    return result


@app.get("/get_max_duration/")
async def get_max_duration(año, plataforma, min_season):
    '''Máxima duración según tipo de film (película/serie), por plataforma y por año'''
    conn = conexion.get_db()
    cursor = conn.cursor()
    if min_season.lower() == 'min':
        df = consultas.Query1(año, plataforma)
        return df
    elif min_season.lower() == 'Season':
        df = consultas.Query1(año, plataforma)
        return df
    elif min_season.lower() == 'Seasons':
        df = consultas.Query1(año, plataforma)
        return df


@app.get("/get_count_plataform/")
async def get_count_plataform(plataforma):
    '''Cantidad de películas y series (separado) por plataforma'''
    conn = conexion.get_db()
    cursor = conn.cursor()
    if plataforma == 'netflix':
        df = consultas.Query2(plataforma)
        return df
    elif plataforma == 'amazon':
        df = consultas.Query2(plataforma)
        return df
    elif plataforma == 'hulu':
        df = consultas.Query2(plataforma)
        return df
    elif plataforma == 'disney plus':
        df = consultas.Query2(plataforma)
        return df

@app.get("/get_listedin/")
async def get_listedin(gen):
    '''Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo'''
    conn = conexion.get_db()
    cursor = conn.cursor()
    if gen == 'Comedy':
        df = consultas.Query3(gen)
        return df


@app.get("/get_actor/")
async def get_actor(plataforma, año):
    '''Cantidad de veces que se repite un actor y la frecuencia del mismo'''
    conn = conexion.get_db()
    cursor = conn.cursor()
    if año == '2018' and plataforma == 'netflix':
        df = consultas.Query4(año, plataforma)
        return df