from zeep import Client

client = Client('http://localhost:8000')

result = client.service.Saludar(nombre="Erick")
print(result)
numero1 = 5;numero2=10
suma = client.service.SumaDosNumeros(numero1, numero2)
print(f"La suma del {numero1} con el {numero2} dara de resultado : {suma}")
cadena="oruro"
caden = client.service.CadenaPalindromo(cadena)
print(f"La palabra {cadena} es palindroma? : {caden}")

