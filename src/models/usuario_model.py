from db import db

usuarios = db.usuarios


def criar_usuario(usuario):
    usuarios.insert_one(usuario)


def criar_usuarios(new_usuarios):
    usuarios.insert_many(new_usuarios)


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


def adicionar_playlist(usuario_id, playlist_id):
    usuarios.update_one({"ID": usuario_id}, {"$push": {"playlists": playlist_id}})


def remover_playlist(usuario_id, playlist_id):
    usuarios.update_one({"ID": usuario_id}, {"$pull": {"playlists": playlist_id}})


def limpar_tabela():
    usuarios.delete_many({})
