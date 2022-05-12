import pymysql.cursors
import pymysql.err
import os
from dotenv import load_dotenv
import logging


load_dotenv()

hostname = os.getenv("HOSTNAME")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")
port = int(os.getenv("PORT"))


def get_mysql_database():
    try:
        myConnection = pymysql.connect( 
                                        host=hostname, 
                                        user=username, 
                                        password=password, 
                                        database=database,
                                        port=port)
    except pymysql.err.InternalError as e:
        logging.debug(str(e))
        print(str(e))
        raise e
   
    return myConnection