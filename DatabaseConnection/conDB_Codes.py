# imports
import mysql.connector
from mysql.connector import Error

# globals
global con, cur

def conDatabase():
    global con, cur
    con = mysql.connector.connect(
        host="nas.awie.at",
        port="8888",
        user="conDB",
        password="conDatabase_DA",
        database="DA_LsgKatalog_Stat"
    )
    cur = con.cursor()

    # test connection
    try:
        if con.is_connected():
            print("Connected")
            print()
    except Error as e:
        print("Error")
        print()