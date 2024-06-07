import json
from flask import Flask, request, jsonify
from models import musica_model, playlist_model, usuario_model
from bson import json_util


def parse_json(data):
    return json.loads(json_util.dumps(data))


app = Flask(__name__)


# API REST para Usuário
@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    usuario = request.json
    usuario_model.criar_usuario(usuario)
    return parse_json({"message": "Usuário criado com sucesso!"}), 201


@app.route("/usuarios", methods=["GET"])
def ler_usuarios():
    print("Lendo usuários")
    usuarios = usuario_model.ler_usuarios()
    return parse_json(usuarios), 200


@app.route("/usuarios/<int:id>", methods=["GET"])
def ler_usuario(id):
    usuario = usuario_model.ler_usuario(id)
    return parse_json(usuario), 200


@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):
    novos_valores = request.json
    usuario_model.atualizar_usuario(id, novos_valores)
    return parse_json({"message": "Usuário atualizado com sucesso!"}), 200


@app.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    usuario_model.deletar_usuario(id)
    return parse_json({"message": "Usuário deletado com sucesso!"}), 200


# API REST para Música
@app.route("/musicas", methods=["POST"])
def criar_musica():
    musica = request.json
    musica_model.criar_musica(musica)
    return parse_json({"message": "Música criada com sucesso!"}), 201


@app.route("/musicas", methods=["GET"])
def ler_musicas():
    musicas = musica_model.ler_musicas()
    return parse_json(musicas), 200


@app.route("/musicas/<int:id>", methods=["GET"])
def ler_musica(id):
    musica = musica_model.ler_musica(id)
    return parse_json(musica), 200


@app.route("/musicas/<int:id>", methods=["PUT"])
def atualizar_musica(id):
    novos_valores = request.json
    musica_model.atualizar_musica(id, novos_valores)
    return parse_json({"message": "Música atualizada com sucesso!"}), 200


@app.route("/musicas/<int:id>", methods=["DELETE"])
def deletar_musica(id):
    musica_model.deletar_musica(id)
    return parse_json({"message": "Música deletada com sucesso!"}), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
