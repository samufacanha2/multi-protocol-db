from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from models import usuario_model


class UsuarioService(ServiceBase):
    @rpc(Integer, Unicode, Integer, _returns=Unicode)
    def criar_usuario(ctx, ID, nome, idade):
        usuario = {"ID": ID, "nome": nome, "idade": idade, "playlists": []}
        usuario_model.criar_usuario(usuario)
        return "Usuário criado com sucesso!"

    @rpc(_returns=Iterable(Unicode))
    def ler_usuarios(ctx):
        usuarios = usuario_model.ler_usuarios()
        return [
            f"ID: {usuario['ID']}, Nome: {usuario['nome']}, Idade: {usuario['idade']}"
            for usuario in usuarios
        ]

    @rpc(Integer, _returns=Iterable(Unicode))
    def ler_usuario(ctx, ID):
        usuario = usuario_model.ler_usuario(ID)
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


# Similar services can be created for Playlist and Música

application = Application(
    [UsuarioService],
    "spyne.examples.flask",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)
    server = make_server("127.0.0.1", 8000, wsgi_app)
    server.serve_forever()
