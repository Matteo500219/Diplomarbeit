# imports
import mysql.connector
from mysql.connector import Error

# globals
global con, cur
tasks = ("all", "first", "last", "specific", "search")


# create connection to database
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

def searchKap(task):
    if task == "all":
        query = "SELECT * FROM `Kapitel`"     # select all data from kapitel
        cur.execute(query)
        ans = cur.fetchall()        # select all items from table
        for r in ans:
            print(r)
    elif task == "first":
        query = "SELECT * FROM `Kapitel`"
        cur.execute(query)
        ans = cur.fetchall()[0]     # select first item from table
        print(ans)
    elif task == "last":
        query = "SELECT * FROM `Kapitel`"
        cur.execute(query)
        ans = cur.fetchall()[-1]    # select last item from table
        print(ans)
    elif type(task) == int:         # means specific number (1., 2., ...)
        num = int(task)
        query = "SELECT * FROM `Kapitel`"
        cur.execute(query)
        ans = cur.fetchall()[num-1]
        print(ans)
    else:                           # search for contained term in complete table
        terms = str(task)
        query = "SELECT * FROM Kapitel WHERE kap_name LIKE %s"
        cur.execute(query, ('%' + terms + '%',))
        ans = cur.fetchall()
        for r in ans:
            print(r)

def searchReg(task):
    if task == "all":
        query = "SELECT * FROM `Region`"
        cur.execute(query)
        ans = cur.fetchall()
        for r in ans:
            print(r)
    if task == "first":
        query = "SELECT * FROM `Region`"
        cur.execute(query)
        ans = cur.fetchall()[0]
        print(ans)
    if task == "last":
        query = "SELECT * FROM `Region`"
        cur.execute(query)
        ans = cur.fetchall()[-1]
        print(ans)
    if type(task) == int:
        num = int(task)
        query = "SELECT * FROM `Region`"
        cur.execute(query)
        ans = cur.fetchall()[num - 1]
        print(ans)

