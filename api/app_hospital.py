from flask import Flask, request, jsonify

pacientes = [
    {"nome": "Maria das Dores", "telefone": "(11) 9573-9839", "convenio": "Amil"},
    {"nome": "Alan Moraes", "telefone": "(11) 9284-0749", "convenio": "Sus"},
    {"nome": "Fernanda Duarte", "telefone": "(11) 9720-8172", "convenio": "Sus"},
    {"nome": "Bianca Souza", "telefone": "(11) 9372-0382", "convenio": "Prevent Senior"}
]

app = Flask("Hospital TDSPR")

@app.route("/paciente", methods=["GET"])
def get_all_pacientes():
    return (pacientes, 200)

@app.route("/paciente/convenio/<convenio>", methods=["GET"])
def get_pacientes_convenio(convenio: str):
    resp = []
    for pac in pacientes:
        if pac['convenio'] == convenio:
            resp.append(pac)
    return (resp, 200)

@app.route("/paciente", methods=["POST"])
def adiciona_paciente():
    info = request.json
    pacientes.append(info)

    resp = {'title': f'Paciente {info["nome"]} cadastrado', 'status': 201}
    return (resp, 201)


app.run(debug=True, host='0.0.0.0')