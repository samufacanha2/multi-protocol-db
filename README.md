# Musica App

Este é um projeto de exemplo que demonstra a implementação de APIs REST, SOAP, gRPC e GraphQL usando Flask, Spyne, Graphene e gRPC. O projeto também inclui uma configuração do Docker para executar a aplicação junto com um banco de dados MongoDB.

## Configuração e Execução

### Pré-requisitos

- Docker
- Docker Compose

### Passos para Configuração

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/musica-app.git
   cd musica-app
   ```

2. Inicie os containers:

   ```bash
   docker-compose up --build
   ```

### Acessando os Serviços

- **API REST**: `http://localhost:5000`
- **API SOAP**: `http://localhost:5001`
- **API GraphQL**: `http://localhost:5002/graphql`
- **API gRPC**: Conecte-se à porta `50051`

## Endpoints

### API REST

- **Criar Usuário**: `POST /usuarios`
- **Ler Usuário**: `GET /usuarios/<id>`
- **Atualizar Usuário**: `PUT /usuarios/<id>`
- **Deletar Usuário**: `DELETE /usuarios/<id>`

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

### API gRPC

Exemplo de cliente gRPC em Python para ler um usuário:

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
