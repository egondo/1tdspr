from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import negocio

app = Flask("API Hospital TDSPR")
CORS(app)

@app.route("/hospital/senha/<cpf>/<nome>", methods=["GET"])
@cross_origin()
def get_senha(cpf: str, nome: str):
    senha = negocio.pega_senha_totem(nome, cpf)
    resp = {"senha": senha, "nome": nome}
    return (resp, 200)


@app.route("/hospital/triagem/<int:senha>", methods=["POST"])
@cross_origin()
def grava_triagem(senha: int):
    triagem = request.json
    print(triagem)
    negocio.grava_triagem(triagem, senha)
    resp = {'title': 'Triagem cadastrada com sucesso', 'status': 200}
    return (resp, 200)

@app.route("/hospital/paciente/<int:senha>", methods=["GET"])
@cross_origin()
def recupera_paciente_senha(senha: int):
    print(f"Senha {senha}" )
    pac = negocio.rec_paciente_senha(senha)
    return (pac, 200)

@app.route("/hospital/paciente", methods=["PUT"])
@cross_origin()
def altera_paciente():
    paciente = request.json
    negocio.atualiza_paciente_recepcao(paciente)
    resp = {"title": "Paciente gravado com sucesso", "status": 200}
    return (resp, 200)

app.run(debug=True)