# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("institutos.db")

# Insertar datos de carreras
conn.execute(
    """
    CREATE TABLE CARRERAS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    duracion INTEGER NOT NULL) ;
    """
)

conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) 
    VALUES ('Ingenieria en informatica', 5)
    """
)

conn.execute(
    """
    INSERT INTO CARRERAS (nombre, duracion) 
    VALUES ('Licenciatura en Administracion', 4)
    """
)
print("CARRERAS:")
cursor = conn.execute("SELECT * FROM CARRERAS")
for row in cursor:
    print(row)
    
conn.execute(
    """
    CREATE TABLE ESTUDIANTES
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL) ;
    """
)
# Insertar datos de estudiantes
conn.execute(
    """
    INSERT INTO ESTUDIANTES 
    (nombre, apellido, fecha_nacimiento) 
    VALUES ('Juan', 'Perez', '2000-05-15')
    """
)
conn.execute(
    """
    INSERT INTO ESTUDIANTES 
    (nombre, apellido, fecha_nacimiento) 
    VALUES ('Maria', 'Lopez', '1999-08-20')
    """
)
# Consultar datos de estudiante
print("\nESTUDIANTES:")
cursor = conn.execute("SELECT * FROM ESTUDIANTES")
for row in cursor:
    print(row)
# Crear tabla matriculacion
conn.execute(
    """
    CREATE TABLE MATRICULACION
        (id INTEGER PRIMARY KEY,
        estudiante_id INTEGER NOT NULL,
        carrera_id INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        FOREIGN KEY (estudiante_id) REFERENCES ESTUDIANTES(id),
        FOREIGN KEY (carrera_id) REFERENCES CARRERAS(id));
    """
)
# Insertar datos de matriculacion
conn.execute(
    """
    INSERT INTO MATRICULACION( estudiante_id, carrera_id, fecha)
    VALUES(1,1,'2024-01-15')
    """    
)
conn.execute(
    """
    INSERT INTO MATRICULACION( estudiante_id, carrera_id, fecha)
    VALUES(2,2,'2024-01-20')
    """    
)
conn.execute(
    """
    INSERT INTO MATRICULACION( estudiante_id, carrera_id, fecha)
    VALUES(1,2,'2024-01-25')
    """    
)
print("\nMatriculacion: ")
cursor = conn.execute(
    """
    SELECT ESTUDIANTES.nombre, ESTUDIANTES.apellido, CARRERAS.nombre, MATRICULACION.fecha
    FROM MATRICULACION
    JOIN ESTUDIANTES ON MATRICULACION.estudiante_id = ESTUDIANTES.id
    JOIN CARRERAS ON MATRICULACION.carrera_id = CARRERAS.id
    """
)
for row in cursor:
    print(row)
#Listar datos de matriculacion
print("\nMATRICULACION")
cursor = conn.execute(
    "SELECT * FROM MATRICULACION"
)
for row in cursor:
    print(row)

#actualizar una fila de la tabla de matriculacion
conn.execute(
    """
    UPDATE MATRICULACION
    SET fecha = '2024-1-30'
    WHERE id = 2
    """
)
# Listar actualizacion de matriculacion
print("\nMATRICULACION: ")
cursor = conn.execute(
    """
    SELECT * FROM MATRICULACION
    """
)
for row in cursor:
    print(row)






# Cerrar conexion
conn.close()
