from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Base de datos simulada de vehículos
chocolates = {}


class FChocolate:
    def __init__(self, choco_type, choco_peso, choco_sabor, choco_relleno):
        self.choco_type = choco_type
        self.choco_peso = choco_peso
        self.choco_sabor = choco_sabor
        self.choco_relleno = choco_relleno
        


class Tableta(FChocolate):
    def __init__(self, choco_peso, choco_sabor):
        super().__init__("tableta", choco_peso, choco_sabor, None)

class Bombones(FChocolate):
    def __init__(self, choco_peso, choco_sabor, choco_relleno):
        super().__init__("bombon", choco_peso, choco_sabor, choco_relleno)

class Trufas(FChocolate):
    def __init__(self, choco_peso, choco_sabor,choco_relleno):
        super().__init__("trufa", choco_peso, choco_sabor,choco_relleno)

class ChocoFactory:
    @staticmethod
    def create_chocolate(choco_type, choco_peso, choco_sabor, choco_relleno):
        if choco_type == "tableta":
            return Tableta(choco_peso, choco_sabor)
        elif choco_type == "bombon":
            return Bombones(choco_peso, choco_sabor, choco_relleno)
        elif choco_type == "trufa":
            return Trufas(choco_peso, choco_sabor, choco_relleno)
        else:
            raise ValueError("Tipo de chocolate no válido")


class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class ChocoService:
    def __init__(self):
        self.factory = ChocoFactory()

    def add_chocolate(self, data):
        choco_type = data.get("choco_type", None)
        choco_peso = data.get("choco_peso", None)
        choco_sabor = data.get("choco_sabor", None)
        choco_relleno = data.get("choco_relleno", None)
        
        fabrica_chocolate = self.factory.create_chocolate(
            choco_type, choco_peso, choco_sabor, choco_relleno
        )
        #index
        
        return fabrica_chocolate

    def list_chocolates(self):
        return {index: chocolate.__dict__ for index, chocolate in chocolates.items()}

    def update_chocolates(self, choco_id, data):
        if choco_id in chocolates:
            chocolate = chocolates[choco_id]
            choco_peso = data.get("choco_peso", None)
            choco_sabor = data.get("choco_sabor", None)
            choco_relleno = data.get("choco_relleno", None)
            if choco_peso:
                chocolate.choco_peso = choco_peso
            if choco_sabor:
                chocolate.choco_sabor = choco_sabor
            if choco_relleno:
                chocolate.choco_relleno = choco_relleno
            return chocolate
        else:
            raise None

    def delete_chocolate(self, chocolate_id):
        if chocolate_id in chocolates:
            del chocolates[chocolate_id]
            return {"message": "chocolate eliminado"}
        else:
            return None


class FabricaRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.chocolate_fabrica = ChocoService()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/chocolates":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.chocolate_fabrica.add_chocolate(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        if self.path == "/chocolates":
            response_data = self.chocolate_fabrica.list_chocolates()
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_PUT(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.chocolate_fabrica.update_chocolates(chocolate_id, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Vehículo no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_DELETE(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1])
            response_data = self.chocolate_fabrica.delete_chocolate(chocolate_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Vehículo no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, FabricaRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()