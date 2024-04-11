import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

new_chocolate_data = {
    "choco_type": "trufa",
    "choco_peso": 300,
    "choco_sabor": "Banana",
    "choco_relleno": "Trago"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)

# GET /deliveries
response = requests.get(url=url)
print("GET")
print(response.json())


# POST /chocolates
new_chocolate_data = {
    "choco_type": "bombon",
    "choco_peso": 100,
    "choco_sabor": "Blanco",
    "choco_relleno": "Gelatina"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print("\nPOST")
print(response.json())

# PUT /deliveries/{chocolate_id}
chocolate_id_to_update = 1
updated_chocolate_data = {
    "choco_peso": 200
}
response = requests.put(f"{url}/{chocolate_id_to_update}", json=updated_chocolate_data)
print("\nChocolate actualizado(PUT):\n", response.json())

# DELETE /deliveries/{chocolate_id}
chocolate_id_to_delete = 1
response = requests.delete(f"{url}/{chocolate_id_to_delete}")
print("\nChocolate eliminado:\n", response.json())
