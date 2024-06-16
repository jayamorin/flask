from flask import Flask, request

app = Flask(__name__)

accounts = []

@app.get("/account")
def get_accounts():
    return accounts

@app.post("/account")
def create_store():
    account_data = request.get_json()

    new_account = {
        "name": account_data["name"],
        "age": account_data["age"],
        "hobby": account_data["hobby"]
    }

    accounts.append(new_account)

    return new_account, 201

@app.get("/account/<string:name>")
def get_store(name):

    for account in accounts:
        if account["name"] == name:
            return account

    return {"message": "Name not found."}, 404


if __name__ == '__main__':
    app.run(debug=True)