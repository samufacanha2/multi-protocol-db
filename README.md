# Acesso à Database Multi-protocolo

Este é um projeto de exemplo que demonstra a implementação de APIs REST, SOAP, gRPC e GraphQL usando Flask, Spyne, Graphene e gRPC. O projeto também inclui uma configuração do Docker para executar a aplicação junto com um banco de dados MongoDB.

## Configuração e Execução

### Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Passos para Configuração

1. Clone este repositório:

   ```bash
   git clone https://github.com/samufacanha2/multi-protocol-db
   cd multi-protocol-db
   ```

2. Inicie os containers:

   ```bash
   docker-compose up --build
   ```

### Acessando os Serviços

- **API REST**: `http://localhost:5000`
- **API SOAP**: `http://localhost:5001`
- **API GraphQL**: `http://localhost:5002/graphql`
- **API gRPC**: Conecte-se à porta `5003`

## Endpoints

### API REST

#### Usuário

- **Criar Usuário**: `POST /usuarios`
- **Ler Usuários**: `GET /usuarios`
- **Ler Usuário**: `GET /usuarios/<id>`
- **Atualizar Usuário**: `PUT /usuarios/<id>`
- **Deletar Usuário**: `DELETE /usuarios/<id>`

#### Música

- **Criar Música**: `POST /musicas`
- **Ler Músicas**: `GET /musicas`
- **Ler Música**: `GET /musicas/<id>`
- **Atualizar Música**: `PUT /musicas/<id>`
- **Deletar Música**: `DELETE /musicas/<id>`

#### Playlist

- **Criar Playlist**: `POST /playlists`
- **Ler Playlists**: `GET /playlists`
- **Ler Playlist**: `GET /playlists/<id>`
- **Atualizar Playlist**: `PUT /playlists/<id>`
- **Deletar Playlist**: `DELETE /playlists/<id>`
- **Listar Playlists de um Usuário**: `GET /usuarios/<usuario_id>/playlists`
- **Listar Músicas de uma Playlist**: `GET /playlists/<playlist_id>/musicas`
- **Listar Playlists por Música**: `GET /musicas/<musica_id>/playlists`

### API SOAP

Exemplo de requisição SOAP para ler um usuário:

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:spy="spyne.examples.flask">
   <soapenv:Header/>
   <soapenv:Body>
      <spy:ler_usuario>
         <spy:ID>1</spy:ID>
      </spy:ler_usuario>
   </soapenv:Body>
</soapenv:Envelope>
```

Exemplo de requisição SOAP para ler uma música:

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:spy="spyne.examples.flask">
   <soapenv:Header/>
   <soapenv:Body>
      <spy:ler_musica>
         <spy:ID>1</spy:ID>
      </spy:ler_musica>
   </soapenv:Body>
</soapenv:Envelope>
```

Exemplo de requisição SOAP para listar as playlists de um usuário:

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:spy="spyne.examples.flask">
   <soapenv:Header/>
   <soapenv:Body>
      <spy:listar_playlists_usuario>
         <spy:usuario_id>1</spy:usuario_id>
      </spy:listar_playlists_usuario>
   </soapenv:Body>
</soapenv:Envelope>
```

### API gRPC

Exemplo de cliente gRPC em Python para ler um usuário:

```python
import grpc
import usuario_pb2
import usuario_pb2_grpc

# Conectar ao servidor gRPC
channel = grpc.insecure_channel('localhost:5003')
stub = usuario_pb2_grpc.UsuarioServiceStub(channel)

# Ler um usuário
usuario = stub.LerUsuario(usuario_pb2.UsuarioID(ID=1))
print(f"ID: {usuario.ID}, Nome: {usuario.nome}, Idade: {usuario.idade}")
```

Exemplo de cliente gRPC em Python para ler uma música:

```python
import grpc
import usuario_pb2
import usuario_pb2_grpc

# Conectar ao servidor gRPC
channel = grpc.insecure_channel('localhost:5003')
stub = usuario_pb2_grpc.MusicaServiceStub(channel)

# Ler uma música
musica = stub.LerMusica(usuario_pb2.MusicaID(ID=1))
print(f"ID: {musica.ID}, Nome: {musica.nome}, Artista: {musica.artista}")
```

Exemplo de cliente gRPC em Python para listar playlists de um usuário:

```python
import grpc
import usuario_pb2
import usuario_pb2_grpc

# Conectar ao servidor gRPC
channel = grpc.insecure_channel('localhost:5003')
stub = usuario_pb2_grpc.PlaylistServiceStub(channel)

# Listar playlists de um usuário
playlists = stub.ListarPlaylistsUsuario(usuario_pb2.UsuarioID(ID=1))
for playlist in playlists.playlists:
    print(f"ID: {playlist.ID}, Nome: {playlist.nome}, Músicas: {playlist.musicas}, Usuário ID: {playlist.usuario_id}")
```

### API GraphQL

Exemplo de query GraphQL para listar todos os usuários:

```graphql
query {
  usuarios {
    ID
    nome
    idade
    playlists
  }
}
```

Exemplo de mutation GraphQL para criar um novo usuário:

```graphql
mutation {
  create_usuario(ID: 2, nome: "User2", idade: 30, playlists: []) {
    message
  }
}
```

Exemplo de query GraphQL para listar todas as músicas:

```graphql
query {
  musicas {
    ID
    nome
    artista
  }
}
```

Exemplo de mutation GraphQL para criar uma nova música:

```graphql
mutation {
  create_musica(ID: 2, nome: "Musica2", artista: "Artista2") {
    message
  }
}
```

Exemplo de query GraphQL para listar todas as playlists de um usuário:

```graphql
query {
  playlists_usuario(usuario_id: 1) {
    ID
    nome
    musicas
    usuario_id
  }
}
```

Exemplo de query GraphQL para listar todas as músicas de uma playlist:

```graphql
query {
  musicas_playlist(playlist_id: 1)
}
```

Exemplo de query GraphQL para listar todas as playlists que contêm uma música:

```graphql
query {
  playlists_por_musica(musica_id: 1) {
    ID
    nome
    musicas
    usuario_id
  }
}
```

Exemplo de mutation GraphQL para criar uma nova playlist:

```graphql
mutation {
  create_playlist(ID: 2, nome: "Playlist2", musicas: [1, 2], usuario_id: 1) {
    message
  }
}
```
