# Importar módulo sqlite3
import sqlite3

# Crear conexión a la base de datos
conn = sqlite3.connect("personal.db")

conn.execute(
        """
        CREATE TABLE CARGOS
        (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        nivel TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL
        );
        """
    )
print("La tabla CARGOS ya existe")

conn.execute(
        """
        CREATE TABLE SALARIOS
        (
        id INTEGER PRIMARY KEY,
        empleado_id INTEGER NOT NULL,
        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion TEXT NOT NULL,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS(id)
        );
        """
    )
print("La tabla SALARIOS ya existe")

conn.execute(
        """
        CREATE TABLE DEPARTAMENTOS
        (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        fecha_creacion TEXT NOT NULL
        );
        """
    )
print("La tabla DEPARTAMENTOS ya existe")
    

conn.execute(
        """
        CREATE TABLE EMPLEADOS
        (
        id INTEGER PRIMARY KEY,
        nombres TEXT NOT NULL,
        departamento_id INTEGER NO NULL,
        cargo_id INTEGER NO NULL,
        apellido_paterno TEXT NOT NULL,
        apellido_materno TEXT NOT NULL,
        fecha_contratacion DATE NOT NULL,
        fecha_creacion TEXT NOT NULL,        
        FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
        FOREIGN KEY (cargo_id) REFERENCES CARGOS(id)
        );
        """
    )
print("La tabla EMPLEADOS ya existe")



conn.execute(
    """
    INSERT INTO DEPARTAMENTOS(nombre, fecha_creacion) 
    VALUES ("Ventas", 10-04-2020)
    """
)
conn.execute(
    """
    INSERT INTO DEPARTAMENTOS(nombre, fecha_creacion) 
    VALUES ("Marketing",11-04-2020)
    """
)

conn.execute(
    """
    INSERT INTO CARGOS(nombre,nivel,fecha_creacion) 
    VALUES ("Gerente de ventas","Senior",10-04-2020)
    """
)

conn.execute(
    """
    INSERT INTO CARGOS(nombre,nivel,fecha_creacion) 
    VALUES ("Analista de Marketing","Junior",11-04-2020)
    """
)
conn.execute(
    """
    INSERT INTO CARGOS(nombre,nivel,fecha_creacion) 
    VALUES ("Representante de ventas","Junior",12-04-2020)
    """
)

#empleados
conn.execute(
    """
    INSERT INTO EMPLEADOS(nombres, departamento_id, cargo_id, apellido_materno, apellido_paterno, fecha_contratacion, fecha_creacion) 
    VALUES ("Juan", 1,1,"Gonzales","Perez",15-05-2023,"")
    """
)

conn.execute(
    """
    INSERT INTO EMPLEADOS(nombres, departamento_id, cargo_id, apellido_materno, apellido_paterno, fecha_contratacion, fecha_creacion) 
    VALUES ("Maria", 1,2,"Lopez","Martinez",20-06-2023,"")
    """
)

conn.execute(
    """
    INSERT INTO SALARIOS(empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) 
    VALUES (1,3000,01-04-2024,30-04-2025,"nose")
    """
    
)

conn.execute(
    """
    INSERT INTO EMPLEADOS(empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) 
    VALUES (1,3000,01-04-2024,30-04-2025,"nose")
    """
    
)


print("\nEMPLEADOS:")
cursor = conn.execute(
    "SELECT EMPLEADOS.NOMBRE FROM "
)
for row in cursor:
    print(row)



# id INTEGER PRIMARY KEY,
#         nombres TEXT NOT NULL,
#         departamento_id INTEGER NO NULL,
#         cargo_id INTEGER NO NULL,
#         apellido_paterno TEXT NOT NULL,
#         apellido_materno TEXT NOT NULL,
#         fecha_contratacion DATE NOT NULL,
#         fecha_creacion TEXT NOT NULL,        
#         FOREIGN KEY (departamento_id) REFERENCES DEPARTAMENTOS(id),
#         FOREIGN KEY (cargo_id) REFERENCES CARGOS(id)
        


# Confirmar cambios
conn.commit()

# Cerrar conexión
conn.close()