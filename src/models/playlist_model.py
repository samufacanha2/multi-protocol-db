from db import db

playlists = db.playlists


def criar_playlist(playlist):
    playlists.insert_one(playlist)


def ler_playlists():
    return list(playlists.find())


def ler_playlist(id):
    return playlists.find_one({"ID": id})


def atualizar_playlist(id, novos_valores):
    playlists.update_one({"ID": id}, {"$set": novos_valores})


def deletar_playlist(id):
    playlists.delete_one({"ID": id})


def listar_playlists_usuario(usuario_id):
    return list(playlists.find({"usuario_id": usuario_id}))


def listar_musicas_playlist(playlist_id):
    playlist = playlists.find_one({"ID": playlist_id})
    if playlist is None:
        return []
    return playlist.get("musicas", [])


def listar_playlists_por_musica(musica_id):
    return list(playlists.find({"musicas": musica_id}))
