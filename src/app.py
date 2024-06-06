from multiprocessing import Process
from apis import rest, soap, graphql


def start_rest_api():
    rest.app.run(port=5000)


def start_soap_api():
    from wsgiref.simple_server import make_server

    wsgi_app = soap.WsgiApplication(soap.application)
    server = make_server("127.0.0.1", 8001, wsgi_app)
    server.serve_forever()


def start_grpc_api():
    from apis.grpc import serve

    serve()


def start_graphql_api():
    graphql.app.run(port=5002)


if __name__ == "__main__":
    processes = [
        Process(target=start_rest_api),
        Process(target=start_soap_api),
        Process(target=start_grpc_api),
        Process(target=start_graphql_api),
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()
