from db import db

musicas = db.musicas


def criar_musica(musica):
    musicas.insert_one(musica)


def ler_musica(id):
    return musicas.find_one({"ID": id})


def atualizar_musica(id, novos_valores):
    musicas.update_one({"ID": id}, {"$set": novos_valores})


def deletar_musica(id):
    musicas.delete_one({"ID": id})
