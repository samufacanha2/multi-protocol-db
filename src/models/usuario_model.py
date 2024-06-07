from db import db

usuarios = db.usuarios


def criar_usuario(usuario):
    usuarios.insert_one(usuario)


def ler_usuario(id):
    usuario_encontrado = usuarios.find_one({"ID": id})
    if usuario_encontrado:
        return usuario_encontrado


def ler_usuarios():
    return list(usuarios.find({}))


def atualizar_usuario(id, novos_valores):
    if ler_usuario(id):
        usuarios.update_one({"ID": id}, {"$set": novos_valores})


def deletar_usuario(id):
    if ler_usuario(id):
        usuarios.delete_one({"ID": id})
