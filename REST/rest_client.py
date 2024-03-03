import requests

url = "http://localhost:8000/"
ruta_get = url + "lista_estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
post_response = requests.request(method="POST", 
                                    url=ruta_post, 
                                    json=nuevo_estudiante)
print(post_response.text)

# buscar_nombre con p
ruta_busNom = url + "buscar_nombre"
bus_nom = requests.request(method="GET", url=ruta_busNom)
print("\nNombres que empiezan con 'P':")
print(bus_nom.text)

# contar_carreras
ruta_contCarr = url + "contar_carreras"
contar_carr = requests.request(method="GET", url=ruta_contCarr)
print("\nCantidad de estudiantes por carrera:")
print(contar_carr.text)

# contar_carreras
ruta_TotalEst = url + "total_estudiantes"
contar_estu = requests.request(method="GET", url=ruta_TotalEst)
print("\nTotal de estudiantes:")
print(contar_estu.text)
