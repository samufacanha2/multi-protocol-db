from models import usuario_model, playlist_model, musica_model


# Exemplos de uso das views
novo_usuario = {"ID": 2, "nome": "User2", "idade": 30, "playlists": []}
usuario_model.criar_usuario(novo_usuario)

usuario_model.ler_usuario(1)

usuario_model.atualizar_usuario(1, {"idade": 26})

usuario_model.deletar_usuario(2)

nova_playlist = {"ID": 1, "nome": "Playlist1", "musicas": [1]}
playlist_model.criar_playlist(nova_playlist)

nova_musica = {"ID": 1, "nome": "Song1", "artista": "Artist1"}
musica_model.criar_musica(nova_musica)
