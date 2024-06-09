from flask import Flask
from flask_graphql import GraphQLView
import graphene
from graphene import ObjectType, String, Int, List, Field, Schema
from models import usuario_model, musica_model, playlist_model


class UsuarioType(ObjectType):
    ID = Int()
    nome = String()
    idade = Int()
    playlists = List(Int)


class MusicaType(ObjectType):
    ID = Int()
    nome = String()
    artista = String()


class PlaylistType(ObjectType):
    ID = Int()
    nome = String()
    musicas = List(Int)
    usuario_id = Int()


class Query(ObjectType):
    usuarios = List(UsuarioType)
    usuario = Field(UsuarioType, ID=Int())
    musicas = List(MusicaType)
    musica = Field(MusicaType, ID=Int())
    playlists = List(PlaylistType)
    playlist = Field(PlaylistType, ID=Int())
    playlists_usuario = List(PlaylistType, usuario_id=Int())
    musicas_playlist = List(Int, playlist_id=Int())
    playlists_por_musica = List(PlaylistType, musica_id=Int())

    def resolve_usuarios(self, info):
        usuarios = usuario_model.ler_usuarios()
        return [
            UsuarioType(
                ID=u["ID"], nome=u["nome"], idade=u["idade"], playlists=u["playlists"]
            )
            for u in usuarios
        ]

    def resolve_usuario(self, info, ID):
        usuario = usuario_model.ler_usuario(ID)
        if not usuario:
            return None
        return UsuarioType(
            ID=usuario["ID"],
            nome=usuario["nome"],
            idade=usuario["idade"],
            playlists=usuario["playlists"],
        )

    def resolve_musicas(self, info):
        musicas = musica_model.ler_musicas()
        return [
            MusicaType(ID=m["ID"], nome=m["nome"], artista=m["artista"])
            for m in musicas
        ]

    def resolve_musica(self, info, ID):
        musica = musica_model.ler_musica(ID)
        if not musica:
            return None
        return MusicaType(
            ID=musica["ID"], nome=musica["nome"], artista=musica["artista"]
        )

    def resolve_playlists(self, info):
        playlists = playlist_model.ler_playlists()
        return [
            PlaylistType(
                ID=p["ID"],
                nome=p["nome"],
                musicas=p["musicas"],
                usuario_id=p["usuario_id"],
            )
            for p in playlists
        ]

    def resolve_playlist(self, info, ID):
        playlist = playlist_model.ler_playlist(ID)
        if not playlist:
            return None
        return PlaylistType(
            ID=playlist["ID"],
            nome=playlist["nome"],
            musicas=playlist["musicas"],
            usuario_id=playlist["usuario_id"],
        )

    def resolve_playlists_usuario(self, info, usuario_id):
        playlists = playlist_model.listar_playlists_usuario(usuario_id)
        return [
            PlaylistType(
                ID=p["ID"],
                nome=p["nome"],
                musicas=p["musicas"],
                usuario_id=p["usuario_id"],
            )
            for p in playlists
        ]

    def resolve_musicas_playlist(self, info, playlist_id):
        return playlist_model.listar_musicas_playlist(playlist_id)

    def resolve_playlists_por_musica(self, info, musica_id):
        playlists = playlist_model.listar_playlists_por_musica(musica_id)
        return [
            PlaylistType(
                ID=p["ID"],
                nome=p["nome"],
                musicas=p["musicas"],
                usuario_id=p["usuario_id"],
            )
            for p in playlists
        ]


class CreateUsuario(graphene.Mutation):
    class Arguments:
        ID = Int(required=True)
        nome = String(required=True)
        idade = Int(required=True)
        playlists = List(Int)

    message = String()

    def mutate(self, info, ID, nome, idade, playlists):
        usuario = {"ID": ID, "nome": nome, "idade": idade, "playlists": playlists}
        usuario_model.criar_usuario(usuario)
        return CreateUsuario(message="Usuário criado com sucesso!")


class CreateMusica(graphene.Mutation):
    class Arguments:
        ID = Int(required=True)
        nome = String(required=True)
        artista = String(required=True)

    message = String()

    def mutate(self, info, ID, nome, artista):
        musica = {"ID": ID, "nome": nome, "artista": artista}
        musica_model.criar_musica(musica)
        return CreateMusica(message="Música criada com sucesso!")


class CreatePlaylist(graphene.Mutation):
    class Arguments:
        ID = Int(required=True)
        nome = String(required=True)
        musicas = List(Int)
        usuario_id = Int(required=True)

    message = String()

    def mutate(self, info, ID, nome, musicas, usuario_id):
        playlist = {
            "ID": ID,
            "nome": nome,
            "musicas": musicas,
            "usuario_id": usuario_id,
        }
        playlist_model.criar_playlist(playlist)
        return CreatePlaylist(message="Playlist criada com sucesso!")


class Mutation(ObjectType):
    create_usuario = CreateUsuario.Field()
    create_musica = CreateMusica.Field()
    create_playlist = CreatePlaylist.Field()


schema = Schema(query=Query, mutation=Mutation)

app = Flask(__name__)
app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
