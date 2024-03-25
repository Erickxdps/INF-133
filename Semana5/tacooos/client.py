import requests

url = "http://localhost:8000/tacos"
headers = {'Content-type': 'application/json'}

mi_taco = {
    "base": "pequeño",
    "guiso": "arto",
    "salsa" : "verde",
    "toppings": ["Tortilla", "Carne molidita"]
}
response = requests.post(url, json=mi_taco, headers=headers)

# GET /tacos
response = requests.get(url)
print("GET/tacos")
print(response.json())

# POST /tacos 
mi_taco = {
    "base": "Grande",
    "guiso": "cochinita pibil",
    "salsa" : "verde cruda",
    "toppings": ["Tortilla", "Carne"]
}
response = requests.post(url, json=mi_taco, headers=headers)
print("\nPOST/tacos")
print(response.json())

# PUT /tacos/1
edit_taco = {
    "base": "de a 5",
    "guiso": "Tinga de pollo",
    "salsa": "Macha",
    "toppings": ["Tortillas", "Pollo"]
}
response = requests.put(url + "/1", json=edit_taco, headers=headers)
print("\nPUT/tacos/1")
print(response.json())

# DELETE /tacos/1
response = requests.delete(url + "/1")
print("\nDELET/tacos/1")
print(response.json())
