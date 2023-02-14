import os
import mysql.connector

def get_db():
    host = os.getenv("MYSQL_HOST", "localhost")
    port = os.getenv("MYSQL_PORT", "3306")
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_PASSWORD", "root")
    database = os.getenv("MYSQL_DATABASE", "pi_dataengineer")
    
    return mysql.connector.connect(
        host = host,
        port = port,
        user = user,
        password = password,
        database = database,
    )
conn = get_db()
cursor = conn.cursor()