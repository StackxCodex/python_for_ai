clients = ["Kelly", "Sierra", "Murriah", "Angela", "Kim"]
clients.append("Ashley")

client = {
    "name": "Ashley",
    "style": "Knotless Braids",
    "price": 220
}
clients.append ({
    "name": "Ashley",
    "style": "Knotless Braids",
    "price": 200
})

for client in clients:
    print(client["name"])

def view_clients():
    for client in clients:
        print(f"{client['name']}" - {client['style']} - "$" + {client: int['price']})