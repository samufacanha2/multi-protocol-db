from db import db

musicas = db.musicas


def criar_musica(musica):
    musicas.insert_one(musica)


def ler_musica(id):
    musica_encontrada = musicas.find_one({"ID": id})
    if musica_encontrada:
        return musica_encontrada


def ler_musicas():
    return list(musicas.find({}))


def atualizar_musica(id, novos_valores):
    if ler_musica(id):
        musicas.update_one({"ID": id}, {"$set": novos_valores})


def deletar_musica(id):
    if ler_musica(id):
        musicas.delete_one({"ID": id})
