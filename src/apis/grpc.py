from concurrent import futures
import grpc
from protobufs import usuario_pb2, usuario_pb2_grpc
from models import usuario_model, musica_model


class UsuarioService(usuario_pb2_grpc.UsuarioServiceServicer):
    def CriarUsuario(self, request, context):
        usuario = {
            "ID": request.ID,
            "nome": request.nome,
            "idade": request.idade,
            "playlists": request.playlists,
        }
        usuario_model.criar_usuario(usuario)
        return usuario_pb2.Resposta(message="Usuário criado com sucesso!")

    def LerUsuario(self, request, context):
        usuario = usuario_model.ler_usuario(request.ID)
        return usuario_pb2.Usuario(
            ID=usuario["ID"],
            nome=usuario["nome"],
            idade=usuario["idade"],
            playlists=usuario["playlists"],
        )

    def AtualizarUsuario(self, request, context):
        novos_valores = {
            "nome": request.nome,
            "idade": request.idade,
            "playlists": request.playlists,
        }
        usuario_model.atualizar_usuario(request.ID, novos_valores)
        return usuario_pb2.Resposta(message="Usuário atualizado com sucesso!")

    def DeletarUsuario(self, request, context):
        usuario_model.deletar_usuario(request.ID)
        return usuario_pb2.Resposta(message="Usuário deletado com sucesso!")

    def LerUsuarios(self, request, context):
        usuarios = usuario_model.ler_usuarios()
        return usuario_pb2.UsuarioList(
            usuarios=[
                usuario_pb2.Usuario(
                    ID=usuario["ID"],
                    nome=usuario["nome"],
                    idade=usuario["idade"],
                    playlists=usuario["playlists"],
                )
                for usuario in usuarios
            ]
        )


class MusicaService(usuario_pb2_grpc.MusicaServiceServicer):
    def CriarMusica(self, request, context):
        musica = {"ID": request.ID, "nome": request.nome, "artista": request.artista}
        musica_model.criar_musica(musica)
        return usuario_pb2.Resposta(message="Música criada com sucesso!")

    def LerMusica(self, request, context):
        musica = musica_model.ler_musica(request.ID)
        return usuario_pb2.Musica(
            ID=musica["ID"], nome=musica["nome"], artista=musica["artista"]
        )

    def AtualizarMusica(self, request, context):
        novos_valores = {"nome": request.nome, "artista": request.artista}
        musica_model.atualizar_musica(request.ID, novos_valores)
        return usuario_pb2.Resposta(message="Música atualizada com sucesso!")

    def DeletarMusica(self, request, context):
        musica_model.deletar_musica(request.ID)
        return usuario_pb2.Resposta(message="Música deletada com sucesso!")

    def LerMusicas(self, request, context):
        musicas = musica_model.ler_musicas()
        return usuario_pb2.MusicaList(
            musicas=[
                usuario_pb2.Musica(
                    ID=musica["ID"], nome=musica["nome"], artista=musica["artista"]
                )
                for musica in musicas
            ]
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    usuario_pb2_grpc.add_UsuarioServiceServicer_to_server(UsuarioService(), server)
    usuario_pb2_grpc.add_MusicaServiceServicer_to_server(MusicaService(), server)
    server.add_insecure_port("[::]:5003")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
