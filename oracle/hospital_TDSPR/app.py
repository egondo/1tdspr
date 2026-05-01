from flask import Flask, request, jsonify
import negocio


app = Flask("API Hospital TDSPR")

@app.route("/hospital/senha/<cpf>/<nome>", methods=["GET"])
def get_senha(cpf: str, nome: str):
    senha = negocio.pega_senha_totem(nome, cpf)
    resp = {"senha": senha, "nome": nome}
    return (resp, 200)


app.run(debug=True)