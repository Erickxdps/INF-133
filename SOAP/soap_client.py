from zeep import Client

client = Client('http://localhost:8000')

result = client.service.Saludar(nombre="Carlitos")
print(result)
suma = client.service.SumaDosNumeros(numero1=5, numero2=10)
print(suma)
caden = client.service.CadenaPalindromo(cadena="oruro")
print(caden)

