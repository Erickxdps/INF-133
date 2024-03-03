import requests

url = "http://localhost:8000/"

# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante ={
        "nombre": "Juanito",
        "apellido": "Perez",
        "carrera": "Ingenieria"
}

post_response = requests.request(method="POST", 
                        url=ruta_post,
                        json=nuevo_estudiante)
print(post_response.text)

nuevo_estudiante = {
    "nombre": "Pedrito",
    "apellido": "Lopez",
    "carrera": "Ingenieria",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)



#agregando 2 estudiantes de economia
nuevo_estudiante = {
    "nombre": "Erick",
    "apellido": "Picavia",
    "carrera": "Economia"
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)
nuevo_estudiante = {
    "nombre": "Carlos",
    "apellido": "Callisaya",
    "carrera": "Economia"
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

#Ejerc
url_carreras = url + "/carreras"
carr = requests.get(url_carreras)
print("\nTodas las carreras:\n", carr.text)


url_economia = url + "/economia"
economicos = requests.get(url_economia)
print("\nEstudiantes de la carrera de economia:\n", economicos.text)