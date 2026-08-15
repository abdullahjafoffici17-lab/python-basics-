# This is simple contact book 
contact = {"name": "Nusky", "phone": "0779853793", "city": "Kandy"}
print(contact["name"])
print(contact["phone"])

contact["city"] = "Anuradhapura"
print(contact)

contact["email"] = "Nusky@gmail.com"
print(contact)

for key in contact:
    print(key, ":", contact[key]) 


# This is multi contact book
contacts = {
    "Fahad": {"phone": "0771234456", "city": "Colombo"},
    "Nusky": {"phone": "0779853793", "city": "Anuradhapura"}
    }

for name in contacts:
    print(name, "lives in", contacts[name]["city"])
