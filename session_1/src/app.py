from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 19.99
            }
        ],
        "location": "manila"
    }
]

@app.get("/store")
def get_stores():
    return stores

@app.post("/store")
def create_store():
    store_data = request.get_json()

    new_store = {
        "name": store_data["name"],
        "items": store_data["items"],
        "location": store_data["location"]
    }

    stores.append(new_store)

    return stores, 201

@app.get("/store/<string:store_name>")
def get_store(store_name):

    for store in stores:
        if store["name"] == store_name:
            return store

@app.post("/store/<string:store_name>/item")
def create_item(store_name):
    item_data = request.get_json()

    for store in stores:
        if store["name"] == store_name:
            new_item = {
                "name": item_data["name"],
                "price": item_data["price"]
            }

            store["items"].append(new_item)
            return store, 201

    return {"message": "Store not found."}, 404

@app.get("/store/<string:store_name>/item")
def get_items_from_stores(store_name):

    for store in stores:
        if store["name"] == store_name:
            return store["items"]

    return {"message": "Store not found."}, 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
