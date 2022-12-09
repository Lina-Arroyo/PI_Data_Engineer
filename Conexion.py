import pymysql
from sqlalchemy import create_engine

cadena_conexion = 'mysql+pymysql://root:@localhost:3306/PI_dataEngineer' 

conexion= create_engine(cadena_conexion) 

conn = conexion.connect()
