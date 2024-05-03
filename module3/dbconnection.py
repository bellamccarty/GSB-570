import psycopg2
import boto3
from psycopg2 import OperationalError
import json

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