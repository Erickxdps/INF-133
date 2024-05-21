# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("ristorante.db")

conn.execute(
    """
    CREATE TABLE PLATOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    categoria TEXT NOT NULL) ;
    """
)
conn.execute(
    """
    INSERT INTO PLATOS (nombre,precio,categoria)
    VALUES ('Pizza',10.99,'Italiana')
    """
)


conn.execute(
    """
    INSERT INTO PLATOS(nombre,precio,categoria)
    VALUES ('Hamburguesa',8.99,'Americana')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS(nombre,precio,categoria)
    VALUES ('Sushi',12.99,'Japonesa')
    """
)
conn.execute(
    """
    INSERT INTO PLATOS(nombre,precio,categoria)
    VALUES ('Ensalada',6.99,'Vegetariana')
    """
)
print("Platos: ")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)



conn.execute(
    """
    CREATE TABLE MESAS
    (id INTEGER PRIMARY KEY,
    numero INTEGER NOT NULL) ;
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (1)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (2)
    """
)
conn.execute(
    """    
    INSERT INTO MESAS (numero)
    VALUES (3)
    """
)
conn.execute(
    """
    INSERT INTO MESAS (numero)
    VALUES (4)
    """
)
print("Mesas: ")
cursor = conn.execute("SELECT * FROM MESAS")
for row in cursor:
    print(row)
    
# PEDIDOS

conn.execute(
    """
    CREATE TABLE PEDIDOS
    (id INTEGER PRIMARY KEY,
    plato_id INTEGER NOT NULL,
    mesa_id INTEGER NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha DATE NOT NULL,
    FOREIGN KEY (plato_id) REFERENCES PLATOS(id),
    FOREIGN KEY (mesa_id) REFERENCES MESAS(id));
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id,mesa_id,cantidad,fecha)
    VALUES (1,2,2,'2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id,mesa_id,cantidad,fecha)
    VALUES (2,3,1,'2024-04-01')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id,mesa_id,cantidad,fecha)
    VALUES (3,1,3,'2024-04-02')
    """
)
conn.execute(
    """
    INSERT INTO PEDIDOS (plato_id,mesa_id,cantidad,fecha)
    VALUES (4,4,1,'2024-04-02')
    """
)

print("Pedidos: ")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)
    
#actualizacion
conn.execute(
    """
    UPDATE PLATOS
    SET precio = 0.99
    WHERE id = 2
    """
)
conn.execute(
    """
    UPDATE PLATOS
    SET categoria = 'Fusion'
    WHERE id = 3
    """
)
conn.execute(
    """
    DELETE FROM PLATOS
    WHERE id = 4
    """
)
conn.execute(
    """
    DELETE FROM PEDIDOS
    WHERE id = 3
    """
)
print("\nPlatos elim and edit: ")
cursor = conn.execute("SELECT * FROM PLATOS")
for row in cursor:
    print(row)

print("\nPedidos elim: ")
cursor = conn.execute("SELECT * FROM PEDIDOS")
for row in cursor:
    print(row)

conn.commit()
conn.close()
