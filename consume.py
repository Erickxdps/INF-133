from zeep import Client 

client = Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)

result1 = client.service.NumberToWords(5)

result = client.service.NumberToDollars(5)

print(result)
print(result1)
