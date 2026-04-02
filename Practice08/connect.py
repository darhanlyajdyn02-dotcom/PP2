import psycopg2
from config import host,dbname,user,port,password

def connect():
    conn = psycopg2.connect(
        host = host,
        dbname = dbname,
        user = user,
        port = port,
        password = password
    )
    return conn