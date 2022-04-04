from flask import Flask,jsonify,request

app = Flask(__name__)

contacts = [
    {
        "Contact":"9840071088",
        "id":1,
        "Name":"Sidarth",
        "done":False
    },
    {
        "Contact":"9677196000",
        "id":2,
        "Name":"Manish",
        "done":False
    }
]
@app.route("/add-data",methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Sorry for the inconvenience"
        },400)
    contact = {
        "id":tasks[-1]["id"]+1,
        "Name":request.json("Name"),
        "Contact":request.json.get("Contact",""),
        "done":False

    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message":"Contact added"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":contacts
    })
if __name__ = "__main__":
    app.run()

        

    