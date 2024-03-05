import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

#Busqueda por nombre con query
ruta_get = url + "estudiantes?nombre=Pedrito&apellido=García"
get_response = requests.request(method="GET", url=ruta_get)
print("\nBUSCAR POR NOMBRE Y APELLIDO")
print(get_response.text)

#Busqueda por apellido con query
ruta_get = url + "estudiantes?apellido=García"
get_response = requests.request(method="GET", url=ruta_get)
print("\nBUSCAR POR APELLIDO")
print(get_response.text)
