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


@app.route("/carros/montadora/<montadora>", methods=["GET"])
def get_carros_montadora(montadora: str):
    resp = []
    for car in db.carros:
        if car['montadora'] == montadora:
            resp.append(car)
    
    if len(resp) == 0:
        info = {"msg": f"Nenhum carro da montadora {montadora} encontrado", "status": 404}
        return (info, 404)
    else:
        return (jsonify(resp), 200)


@app.route("/carros", methods=["POST"])
def insere_carro():
    novo_carro = request.json
    for i in range(len(db.carros)):
        if novo_carro['id'] == db.carros[i]['id']:
            info = {
                "msg": "Impossível adicionar, carro ja existe",
                "status": 406
            }
            return (jsonify(info), 406)
    db.carros.append(novo_carro)
    return (jsonify(novo_carro), 201)







app.run(debug=True)