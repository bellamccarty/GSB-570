import psycopg2
import os
from psycopg2 import OperationalError
from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv('DBNAME')
db_user =  os.getenv('DBUSER')
db_password = os.getenv('PASSWORD')
db_host = os.getenv('HOST')
db_port = "5432"

def open_connection_to_db():
    # surround with try catch   
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
    except OperationalError as e:
        print(f"Error connecting to database: {e}")
        conn = None 

    return conn

def get_db_attributes():
    print(db_name, db_user, db_password, db_host, db_port)