from multiprocessing import Process
from apis import rest, soap, graphql
from db_init import db_init


def start_rest_api():
    rest.app.run(host="0.0.0.0", port=5000)


def start_soap_api():
    from wsgiref.simple_server import make_server

    wsgi_app = soap.WsgiApplication(soap.application)
    server = make_server("0.0.0.0", 5001, wsgi_app)  # type: ignore
    server.serve_forever()


def start_grpc_api():
    from apis.grpc import serve

    serve()


def start_graphql_api():
    graphql.app.run(port=5002, host="0.0.0.0")


if __name__ == "__main__":
    db_init()

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
