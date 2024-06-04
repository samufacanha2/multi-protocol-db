from db import db

playlists = db.playlists


def criar_playlist(playlist):
    playlists.insert_one(playlist)


def ler_playlist(id):
    return playlists.find_one({"ID": id})


def atualizar_playlist(id, novos_valores):
    playlists.update_one({"ID": id}, {"$set": novos_valores})


def deletar_playlist(id):
    playlists.delete_one({"ID": id})
