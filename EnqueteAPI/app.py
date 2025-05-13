from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import negocio

app = Flask(__name__)
CORS(app, origins="http://127.0.0.1:5000")

@app.route("/perguntas/<int:enquete_id>", methods=["GET"])
@cross_origin()
def recupera_perguntas(enquete_id: int) -> list:
    dados = negocio.recupera_perguntas(enquete_id)
    return (jsonify(dados), 200)


@app.route("/respostas", methods=["POST"])
@cross_origin()
def grava_respostas():
    info = request.json
    print(info)
    dados = "{'msg': 'dados cadastrados}"
    return (jsonify(dados), 201)


app.run(debug=True)