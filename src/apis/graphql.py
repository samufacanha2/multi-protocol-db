from flask import Flask
from flask_graphql import GraphQLView
import graphene
from graphene import ObjectType, String, Int, List, Field, Schema
from models import usuario_model


class UsuarioType(ObjectType):
    ID = Int()
    nome = String()
    idade = Int()
    playlists = List(Int)


class Query(ObjectType):
    usuarios = List(UsuarioType)
    usuario = Field(UsuarioType, ID=Int())

    def resolve_usuarios(parent, info):
        usuarios = usuario_model.ler_usuarios()
        return [
            UsuarioType(
                ID=u["ID"], nome=u["nome"], idade=u["idade"], playlists=u["playlists"]
            )
            for u in usuarios
        ]

    def resolve_usuario(parent, info, ID):
        usuario = usuario_model.ler_usuario(ID)
        return UsuarioType(
            ID=usuario["ID"],
            nome=usuario["nome"],
            idade=usuario["idade"],
            playlists=usuario["playlists"],
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


class Mutation(ObjectType):
    create_usuario = CreateUsuario.Field()


schema = Schema(query=Query, mutation=Mutation)

app = Flask(__name__)
app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
