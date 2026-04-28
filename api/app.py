from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/saudacao/<idioma>", methods=["GET"])
def hello_world(idioma: str):
    if idioma == "portugues":
        return ("Olá mundo!", 200)
    elif idioma == "ingles":
        return ("Hello World!", 200)
    elif idioma == "japones":
        return ("Kon'nichiwa sekai!", 200)
    elif idioma == "russo":
        return ("Privet, mir!", 200)
    else:
        info = {'title': 'Idioma não encontrado', 'status_code': 404}
        return (info, 404)

if __name__ == "__main__":
    app.run(debug=True)