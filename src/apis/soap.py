from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from models import usuario_model, musica_model


class UsuarioService(ServiceBase):
    @rpc(Integer, Unicode, Integer, _returns=Unicode)
    def criar_usuario(ctx, ID, nome, idade):
        usuario = {"ID": ID, "nome": nome, "idade": idade, "playlists": []}
        usuario_model.criar_usuario(usuario)
        return "Usuário criado com sucesso!"

    @rpc(Integer, _returns=Iterable(Unicode))
    def ler_usuario(ctx, ID):
        usuario = usuario_model.ler_usuario(ID)
        if not usuario:
            return ["Usuário não encontrado!"]
        return [
            f"ID: {usuario['ID']}",
            f"Nome: {usuario['nome']}",
            f"Idade: {usuario['idade']}",
        ]

    @rpc(Integer, Unicode, Integer, _returns=Unicode)
    def atualizar_usuario(ctx, ID, nome, idade):
        novos_valores = {"nome": nome, "idade": idade}
        usuario_model.atualizar_usuario(ID, novos_valores)
        return "Usuário atualizado com sucesso!"

    @rpc(Integer, _returns=Unicode)
    def deletar_usuario(ctx, ID):
        usuario_model.deletar_usuario(ID)
        return "Usuário deletado com sucesso!"

    @rpc(_returns=Iterable(Unicode))
    def ler_usuarios(ctx):
        usuarios = usuario_model.ler_usuarios()
        return [
            f"ID: {usuario['ID']}, Nome: {usuario['nome']}, Idade: {usuario['idade']}"
            for usuario in usuarios
        ]


class MusicaService(ServiceBase):
    @rpc(Integer, Unicode, Unicode, _returns=Unicode)
    def criar_musica(ctx, ID, nome, artista):
        musica = {"ID": ID, "nome": nome, "artista": artista}
        musica_model.criar_musica(musica)
        return "Música criada com sucesso!"

    @rpc(Integer, _returns=Iterable(Unicode))
    def ler_musica(ctx, ID):
        musica = musica_model.ler_musica(ID)
        if not musica:
            return ["Música não encontrada!"]
        return [
            f"ID: {musica['ID']}",
            f"Nome: {musica['nome']}",
            f"Artista: {musica['artista']}",
        ]

    @rpc(Integer, Unicode, Unicode, _returns=Unicode)
    def atualizar_musica(ctx, ID, nome, artista):
        novos_valores = {"nome": nome, "artista": artista}
        musica_model.atualizar_musica(ID, novos_valores)
        return "Música atualizada com sucesso!"

    @rpc(Integer, _returns=Unicode)
    def deletar_musica(ctx, ID):
        musica_model.deletar_musica(ID)
        return "Música deletada com sucesso!"

    @rpc(_returns=Iterable(Unicode))
    def ler_musicas(ctx):
        musicas = musica_model.ler_musicas()
        return [
            f"ID: {musica['ID']}, Nome: {musica['nome']}, Artista: {musica['artista']}"
            for musica in musicas
        ]


application = Application(
    [UsuarioService, MusicaService],
    "spyne.examples.flask",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)
    server = make_server("0.0.0.0", 5001, wsgi_app)  # type: ignore
    server.serve_forever()
