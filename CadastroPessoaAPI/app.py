from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import negocio

app = Flask("API de Pessoa")
CORS(app, origins="http://127.0.0.1:5000")


@app.route("/pessoas", methods=["POST"])
@cross_origin()
def grava_pessoa():
    dados = request.json
    try:
        pes = dados['pessoa']
        end = dados['endereco']
        negocio.cadastra_pessoa(pes, end)
        return (dados, 201)
    except:
        info = {"title": "erro no cadastramento", 
                "status": 400}
        return (info, 400)

app.run(debug=True)