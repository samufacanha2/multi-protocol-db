from db import db

usuarios = db.usuarios


def criar_usuario(usuario):
    usuarios.insert_one(usuario)


def ler_usuario(id):
    return usuarios.find_one({"ID": id})


def atualizar_usuario(id, novos_valores):
    usuarios.update_one({"ID": id}, {"$set": novos_valores})


def deletar_usuario(id):
    usuarios.delete_one({"ID": id})
