from flask import Flask, request, jsonify
import negocio

app = Flask("API de Pessoa")

@app.route("/pessoas", methods=["POST"])
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