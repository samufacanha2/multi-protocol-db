from flask import Flask
from flask_graphql import GraphQLView
import graphene
from graphene import ObjectType, String, Int, List, Field, Schema
from models import usuario_model, musica_model


class UsuarioType(ObjectType):
    ID = Int()
    nome = String()
    idade = Int()
    playlists = List(Int)


class MusicaType(ObjectType):
    ID = Int()
    nome = String()
    artista = String()


class Query(ObjectType):
    usuarios = List(UsuarioType)
    usuario = Field(UsuarioType, ID=Int())
    musicas = List(MusicaType)
    musica = Field(MusicaType, ID=Int())

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


class Mutation(ObjectType):
    create_usuario = CreateUsuario.Field()
    create_musica = CreateMusica.Field()


schema = Schema(query=Query, mutation=Mutation)

app = Flask(__name__)
app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
