#Fase 5
from fastapi import FastAPI
from starlette.responses import RedirectResponse
import querys as consultas
import Conexion as conn

app = FastAPI(title="API consultas PI data engineer",)

@app.get("/get_max_duration/")
async def get_max_duration(año, plataforma, min_season):
    '''Máxima duración según tipo de film (película/serie), por plataforma y por año'''
    if min_season.lower() == 'min':
        df = consultas.Query1(conn, año, plataforma.capitalize())
        return df.to_dict('r')
    elif min_season.lower() == 'Season':
        df = consultas.Query1(conn, año, plataforma.capitalize())
        return df.to_dict('r')
    elif min_season.lower() == 'Seasons':
        df = consultas.Query1(conn, año, plataforma.capitalize())
        return df.to_dict('r')


@app.get("/get_count_plataform/")
async def get_count_plataform(plataforma):
    '''Cantidad de películas y series (separado) por plataforma'''
    if plataforma == 'netflix':
        df = consultas.Query2(conn, plataforma.capitalize())
        return df.to_dict('r')
    elif plataforma == 'amazon':
        df = consultas.Query2(conn, plataforma.capitalize())
        return df.to_dict('r')
    elif plataforma == 'hulu':
        df = consultas.Query2(conn, plataforma.capitalize())
        return df.to_dict('r')
    elif plataforma == 'disney plus':
        df = consultas.Query2(conn, plataforma.capitalize())
        return df.to_dict('r')

@app.get("/get_listedin/")
async def get_listedin(gen):
    '''Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo'''
    if gen == 'Comedy':
        df = consultas.Query3(conn, gen.capitalize(), )
        return df.to_dict('r')


@app.get("/get_actor/")
async def get_actor(plataf, anio):
    '''Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo'''
    if anio == '2018':
        df = consultas.Query4(conn, anio, plataf)
        return df.to_dict('r')