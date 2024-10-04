import mysql.connector

# Connection to database
connection = mysql.connector.connect(
    host="192.168.1.195",   # IP of the server
    user="try",
    password="trypassword",
    database="DA_LsgKatalog"
)

# Create database DA_Try
def createDatabase():
    cur = connection.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS DA_LsgKatalog")
    cur.execute("USE DA_LsgKatalog")       # If exists, use it

def createTable():
    cur = connection.cursor()

    # Create table Kapitel
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Kapitel (
            kap_id INT(11) PRIMARY KEY,
            kap_name VARCHAR(80) NOT NULL
        )
    """)

    # Create table Region
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Region (
            reg_id INT(11), 
            kap_id INT(11), 
            reg_name VARCHAR(80) NOT NULL,
            PRIMARY KEY (reg_id, kap_id), 
            FOREIGN KEY (kap_id) REFERENCES Kapitel(kap_id) ON UPDATE CASCADE ON DELETE CASCADE
        )   
    """)

    # Create table Code
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Code (
            code_id INT(11) PRIMARY KEY,
            code_name VARCHAR(400) NOT NULL,
            kap_id INT(11) NOT NULL, 
            reg_id INT(11) NOT NULL, 
            FOREIGN KEY (reg_id, kap_id) REFERENCES Region(reg_id, kap_id) ON UPDATE CASCADE ON DELETE CASCADE
        )
    """)

# Beispiel-Daten hinzufügen
def insert_data(connection):
    cursor = connection.cursor()
    """
    # Insert data into Kapitel
    kapitel_data = [
        (1, "Nervensystem, Psyche, Gehirnschädel, Wirbelsäule"),
        (2, "Augen und Orbita"),
        (3, "Ohren, Nase, Mundhöhle, Rachen, Gesicht, Gesichtsschädel, Hals")
    ]
    cursor.executemany("INSERT INTO Kapitel (kap_id, kap_name) VALUES (%s, %s)", kapitel_data)
    """
    # Insert data into Region
    region_data = [
        (1, 1, "Operationen an Gehirnschädel und Dura"),  # Kapitel 1
        (1, 2, "Intrakranielle Operationen"),  # Kapitel 1
        (2, 1, "Operationen an Bindehaut, Lidern und Tränenwegen"),  # Kapitel 2
        (2, 3, "Operationen an Glaskörper und Retina"),  # Kapitel 2
        (3, 2, "Operationen am Mittelohr")  # Kapitel 3
    ]
    cursor.executemany("INSERT INTO Region (reg_id, kap_id, reg_name) VALUES (%s, %s, %s)", region_data)
    """
    # Insert data into Code
    code_data = [
        # Bereich 01.01: Zwei Codes für diesen Bereich
        (1, "Operation am Gehirnschädel mit kranieller Fixation", 1, 1),
        (2, "Minimalinvasive Operation an der Schädeldecke", 1, 1),

        # Bereich 01.02: Ein Code für diesen Bereich
        (3, "Intrakranielle Entfernung eines Tumors", 1, 2),

        # Bereich 02.01: Ein Code für diesen Bereich
        (4, "Operation an der Bindehaut mit Hornhauttransplantation", 2, 1),

        # Bereich 02.03: Ein Code für diesen Bereich
        (5, "Vitrektomie mit Netzhautablösung", 2, 3),

        # Bereich 03.02: Ein Code für diesen Bereich
        (6, "Tympanoplastik bei Mittelohrentzündung", 3, 2)
    ]
    cursor.executemany("INSERT INTO Code (code_id, code_name, kap_id, reg_id) VALUES (%s, %s, %s, %s)", code_data)
    """
    connection.commit()

insert_data(connection)
