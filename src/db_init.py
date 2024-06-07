from models import musica_model, playlist_model, usuario_model


def db_init():
    novo_usuario = {"ID": 2, "nome": "User2", "idade": 30, "playlists": []}
    if not usuario_model.ler_usuario(2):
        usuario_model.criar_usuario(novo_usuario)


# nova_playlist = {"ID": 1, "nome": "Playlist1", "musicas": [1]}
# playlist_model.criar_playlist(nova_playlist)

# nova_musica = {"ID": 1, "nome": "Song1", "artista": "Artist1"}
# musica_model.criar_musica(nova_musica)
