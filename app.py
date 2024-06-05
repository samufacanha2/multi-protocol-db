from apis import rest, soap

# Start the REST API server
from multiprocessing import Process


def start_rest():
    rest.app.run(port=5000)


def start_soap():
    from wsgiref.simple_server import make_server

    wsgi_app = soap.WsgiApplication(soap.application)
    server = make_server("127.0.0.1", 8001, wsgi_app)
    server.serve_forever()


if __name__ == "__main__":
    rest_process = Process(target=start_rest)
    soap_process = Process(target=start_soap)

    rest_process.start()
    soap_process.start()

    rest_process.join()
    soap_process.join()
