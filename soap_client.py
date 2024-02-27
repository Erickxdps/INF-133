from zeep import Client

client = Client('http://localhost:8000')

result = client.service.Saludar(nombre="Carlitos")
print(result)

suma = client.service.SumaDosNumeros(numero1=5, numero2=10)
print(suma)










#wsdl_url = "https://www.dataaccess.com/webservicesserver/numberconversion.wso?WSDL"

# Crea un cliente SOAP basado en el WSDL
#client = Client(wsdl_url)

# Llama a la función NumberToDollars con un número como argumento
#result = client.service.NumberToDollars(123.45)
#print(result)