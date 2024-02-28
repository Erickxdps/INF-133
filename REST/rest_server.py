from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import requests


estudiantes = [
    {
        "id": 1,
        "nombre": "Erick",
        "apellido": "Picavia",
        "carrera": "Ingenieria",
    },
    {
        "id": 2,
        "nombre": "Pedro",
        "apellido": "Perez",
        "carrera": "Ingenieria",
    },
    {
        "id": 3,
        "nombre": "Pablo",
        "apellido": "Gomez",
        "carrera": "Matematicas",
    },
    {
        "id": 4,
        "nombre": "Maria",
        "apellido": "Gonzalez",
        "carrera": "Biologia",
    },
    {
        "id": 5,
        "nombre": "Juan",
        "apellido": "Martinez",
        "carrera": "Matematicas",
    },
    {
        "id": 6,
        "nombre": "Laura",
        "apellido": "Rodriguez",
        "carrera": "Ingenieria",
    },
    {
        "id": 7,
        "nombre": "Carlos",
        "apellido": "López",
        "carrera": "Biologia",
    },
    {
        "id": 8,
        "nombre": "Sofia",
        "apellido": "Hernandez",
        "carrera": "Medicina",
    },
    {
        "id": 9,
        "nombre": "Diego",
        "apellido": "Diaz",
        "carrera": "Medicina",
    },
    {
        "id": 10,
        "nombre": "Ana",
        "apellido": "Pérez",
        "carrera": "Biologia",
    },
    {
        "id": 11,
        "nombre": "Javier",
        "apellido": "Sanchez",
        "carrera": "Ingenieria",
    },
    {
        "id": 12,
        "nombre": "Elena",
        "apellido": "Ramirez",
        "carrera": "Matematicas",
    },
    {
        "id": 13,
        "nombre": "Andrés",
        "apellido": "Flores",
        "carrera": "Medicina",
    }
]


class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/lista_estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
        elif self.path == '/buscar_nombre':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            nombres_con_p = self.buscar_nombre()
            self.wfile.write(json.dumps({"Nombres con P": nombres_con_p}).encode('utf-8'))
        elif self.path == '/contar_carreras':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            conteo_carreras = self.contar_carreras()
            self.wfile.write(json.dumps(conteo_carreras).encode('utf-8'))
        elif self.path == '/total_estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            total_estudiantes = len(estudiantes)
            self.wfile.write(json.dumps({"Total de estudiantes": total_estudiantes}).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))
            
    def do_POST(self):
        if self.path == '/agrega_estudiante':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode('utf-8'))
            post_data['id'] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8'))
            self.buscar_nombre()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))
    #Bucar nombres con p:            
    def buscar_nombre(self):
        nombres_con_p = [estudiante["nombre"] for estudiante in estudiantes if estudiante["nombre"].startswith("P")]
        return nombres_con_p
    #Contar estudiantes por carrera
    def contar_carreras(self):
        conteo_carreras = {}
        for estudiante in estudiantes:
            carrera = estudiante["carrera"]
            if carrera in conteo_carreras:
                conteo_carreras[carrera] += 1
            else:
                conteo_carreras[carrera] = 1
        return conteo_carreras
    
def run_server(port = 8000):
    try:
        server_address = ('', port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f'Iniciando servidor web en http://localhost:{port}/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando servidor web')
        httpd.socket.close()

if __name__ == "__main__":
    run_server()
