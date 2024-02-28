from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
    return "¡Hola, {}!".format(nombre)

def SumaDosNumeros(numero1, numero2):
    return numero1 + numero2

def CadenaPalindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo": str},
    args={"nombre": str},
)

dispatcher.register_function(
    "SumaDosNumeros",
    SumaDosNumeros,
    returns={"resultado": int},
    args={"numero1": int, "numero2": int},
)

dispatcher.register_function(
    "CadenaPalindromo",
    CadenaPalindromo,
    returns={"es_palindromo": bool},
    args={"cadena": str},
)

server = HTTPServer(("", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciando en http://localhost:8000/")
server.serve_forever()
