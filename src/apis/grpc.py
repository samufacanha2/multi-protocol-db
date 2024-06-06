from concurrent import futures
import grpc
from protobufs import usuario_pb2, usuario_pb2_grpc
from models import usuario_model


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


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    usuario_pb2_grpc.add_UsuarioServiceServicer_to_server(UsuarioService(), server)
    print("Servidor gRPC rodando na porta 50051")
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
