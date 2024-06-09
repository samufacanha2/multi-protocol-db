from concurrent import futures
import grpc
from protobufs import dtos_pb2, dtos_pb2_grpc
from models import usuario_model, musica_model, playlist_model


class UsuarioService(dtos_pb2_grpc.UsuarioServiceServicer):
    def CriarUsuario(self, request, context):
        usuario = {
            "ID": request.ID,
            "nome": request.nome,
            "idade": request.idade,
            "playlists": request.playlists,
        }
        usuario_model.criar_usuario(usuario)
        return dtos_pb2.Resposta(message="Usuário criado com sucesso!")

    def LerUsuario(self, request, context):
        usuario = usuario_model.ler_usuario(request.ID)
        return dtos_pb2.Usuario(
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
        return dtos_pb2.Resposta(message="Usuário atualizado com sucesso!")

    def DeletarUsuario(self, request, context):
        usuario_model.deletar_usuario(request.ID)
        return dtos_pb2.Resposta(message="Usuário deletado com sucesso!")

    def LerUsuarios(self, request, context):
        usuarios = usuario_model.ler_usuarios()
        return dtos_pb2.UsuarioList(
            usuarios=[
                dtos_pb2.Usuario(
                    ID=usuario["ID"],
                    nome=usuario["nome"],
                    idade=usuario["idade"],
                    playlists=usuario["playlists"],
                )
                for usuario in usuarios
            ]
        )


class MusicaService(dtos_pb2_grpc.MusicaServiceServicer):
    def CriarMusica(self, request, context):
        musica = {"ID": request.ID, "nome": request.nome, "artista": request.artista}
        musica_model.criar_musica(musica)
        return dtos_pb2.Resposta(message="Música criada com sucesso!")

    def LerMusica(self, request, context):
        musica = musica_model.ler_musica(request.ID)
        return dtos_pb2.Musica(
            ID=musica["ID"], nome=musica["nome"], artista=musica["artista"]
        )

    def AtualizarMusica(self, request, context):
        novos_valores = {"nome": request.nome, "artista": request.artista}
        musica_model.atualizar_musica(request.ID, novos_valores)
        return dtos_pb2.Resposta(message="Música atualizada com sucesso!")

    def DeletarMusica(self, request, context):
        musica_model.deletar_musica(request.ID)
        return dtos_pb2.Resposta(message="Música deletada com sucesso!")

    def LerMusicas(self, request, context):
        musicas = musica_model.ler_musicas()
        return dtos_pb2.MusicaList(
            musicas=[
                dtos_pb2.Musica(
                    ID=musica["ID"], nome=musica["nome"], artista=musica["artista"]
                )
                for musica in musicas
            ]
        )


class PlaylistService(dtos_pb2_grpc.PlaylistServiceServicer):
    def CriarPlaylist(self, request, context):
        playlist = {
            "ID": request.ID,
            "usuario_id": request.usuario_id,
            "musicas": list(request.musicas),
        }
        playlist_model.criar_playlist(playlist)
        return dtos_pb2.Resposta(message="Playlist criada com sucesso!")

    def ListarPlaylistsPorUsuario(self, request, context):
        playlists = playlist_model.listar_playlists_usuario(request.ID)
        return dtos_pb2.PlaylistList(
            playlists=[
                dtos_pb2.Playlist(
                    ID=playlist["ID"],
                    usuario_id=playlist["usuario_id"],
                    musicas=playlist["musicas"],
                )
                for playlist in playlists
            ]
        )

    def ListarMusicasPorPlaylist(self, request, context):
        musicas = playlist_model.listar_musicas_playlist(request.ID)
        return dtos_pb2.MusicaList(
            musicas=[
                dtos_pb2.Musica(
                    ID=musica["ID"], nome=musica["nome"], artista=musica["artista"]
                )
                for musica in musicas
            ]
        )

    def ListarPlaylistsPorMusica(self, request, context):
        playlists = playlist_model.listar_playlists_por_musica(request.ID)
        return dtos_pb2.PlaylistList(
            playlists=[
                dtos_pb2.Playlist(
                    ID=playlist["ID"],
                    usuario_id=playlist["usuario_id"],
                    musicas=playlist["musicas"],
                )
                for playlist in playlists
            ]
        )

    def LerPlaylist(self, request, context):
        playlist = playlist_model.ler_playlist(request.ID)
        return dtos_pb2.Playlist(
            ID=playlist["ID"],
            usuario_id=playlist["usuario_id"],
            musicas=playlist["musicas"],
        )

    def AtualizarPlaylist(self, request, context):
        novos_valores = {
            "usuario_id": request.usuario_id,
            "musicas": list(request.musicas),
        }
        playlist_model.atualizar_playlist(request.ID, novos_valores)
        return dtos_pb2.Resposta(message="Playlist atualizada com sucesso!")

    def DeletarPlaylist(self, request, context):
        playlist_model.deletar_playlist(request.ID)
        return dtos_pb2.Resposta(message="Playlist deletada com sucesso!")

    def LerPlaylists(self, request, context):
        playlists = playlist_model.ler_playlists()
        return dtos_pb2.PlaylistList(
            playlists=[
                dtos_pb2.Playlist(
                    ID=playlist["ID"],
                    usuario_id=playlist["usuario_id"],
                    musicas=playlist["musicas"],
                )
                for playlist in playlists
            ]
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dtos_pb2_grpc.add_UsuarioServiceServicer_to_server(UsuarioService(), server)
    dtos_pb2_grpc.add_MusicaServiceServicer_to_server(MusicaService(), server)
    dtos_pb2_grpc.add_PlaylistServiceServicer_to_server(PlaylistService(), server)

    server.add_insecure_port("[::]:5003")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
