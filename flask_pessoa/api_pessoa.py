from flask import Flask, request, jsonify

import negocio

app = Flask(__name__)

@app.route("/pessoas", methods=['POST'])
def cad_pessoa():
    try:
        pessoa = request.json
        negocio.cadastra_pessoa(pessoa)
        return (jsonify(pessoa), 201)
    except:
        info = {
            'title': "Erro no cadastramento de pessoa",
            "status": 400
        }
        return (jsonify(info), 400)

@app.route("/pessoas", methods=['GET'])
def rec_pessoas():
    try:
        dados = negocio.recupera_todas_pessoas()
        return (jsonify(dados), 200)
    except:
        info = {
            'title': "Erro na consulta de pessoa",
            "status": 400
        }
        return (jsonify(info), 400)


app.run(debug=True)