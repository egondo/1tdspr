from flask import Flask, jsonify, request
import db

app = Flask(__name__)

@app.route("/carros", methods=["GET"])
def get_all_carros():
    return (db.carros, 200)


@app.route("/carros/<int:id>", methods=["GET"])
def get_carro(id: int):
    for car in db.carros:
        if car['id'] == id:
            return (jsonify(car), 200)
    
    info = {
        "msg": f"Nenhum carro com id {id} encontrado", 
        "status": 404
    }
    return (info, 404)



app.run(debug=True)