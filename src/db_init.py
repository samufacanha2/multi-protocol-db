from models import musica_model, playlist_model, usuario_model
import random


# Limpar coleções existentes
usuario_model.limpar_tabela()
musica_model.limpar_tabela()
playlist_model.limpar_tabela()


# Funções para gerar dados aleatórios
def gerar_nome_aleatorio():
    nomes = ["Alice", "Bob", "Carol", "David", "Eve", "Frank", "Grace", "Heidi"]
    sobrenomes = [
        "Smith",
        "Johnson",
        "Williams",
        "Jones",
        "Brown",
        "Davis",
        "Miller",
        "Wilson",
    ]
    return f"{random.choice(nomes)} {random.choice(sobrenomes)}"


def gerar_musica_aleatoria():
    titulos = ["Song1", "Song2", "Song3", "Song4", "Song5", "Song6", "Song7", "Song8"]
    artistas = [
        "Artist1",
        "Artist2",
        "Artist3",
        "Artist4",
        "Artist5",
        "Artist6",
        "Artist7",
        "Artist8",
    ]
    return {
        "ID": random.randint(1, 1000),
        "nome": random.choice(titulos),
        "artista": random.choice(artistas),
    }


def gerar_playlist_aleatoria(usuario_id, musicas_ids):
    titulos = [
        "Playlist1",
        "Playlist2",
        "Playlist3",
        "Playlist4",
        "Playlist5",
        "Playlist6",
        "Playlist7",
        "Playlist8",
    ]
    num_musicas = random.randint(1, len(musicas_ids))
    return {
        "ID": random.randint(1, 1000),
        "nome": random.choice(titulos),
        "musicas": random.sample(musicas_ids, num_musicas),
        "usuario_id": usuario_id,
    }


def db_init():
    usuarios = []
    musicas = []
    playlists = []

    for i in range(10):
        usuario = {
            "ID": i + 1,
            "nome": gerar_nome_aleatorio(),
            "idade": random.randint(18, 60),
            "playlists": [],
        }
        usuarios.append(usuario)

    usuario_model.criar_usuarios(usuarios)

    for i in range(50):
        musica = gerar_musica_aleatoria()
        musicas.append(musica)

    musica_model.criar_musicas(musicas)

    musicas_ids = [musica["ID"] for musica in musicas]

    for usuario in usuarios:
        num_playlists = random.randint(1, 5)
        for _ in range(num_playlists):
            playlist = gerar_playlist_aleatoria(usuario["ID"], musicas_ids)
            playlists.append(playlist)

    playlist_model.criar_playlists(playlists)

    print("Banco de dados de teste gerado com sucesso!")
