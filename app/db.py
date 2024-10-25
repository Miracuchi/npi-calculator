import psycopg2
from psycopg2 import sql
def get_connection():
    connection = psycopg2.connect(
        dbname = "",
        user= "postgres",
        password = "postgres",
        host = "localhost",
        port = "5432"
    )
    return connection