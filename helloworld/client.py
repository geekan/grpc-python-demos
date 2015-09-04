#!/usr/local/bin/grun

import helloworld_pb2

_TIMEOUT_SECONDS = 10


def run():
    with helloworld_pb2.early_adopter_create_helloworld_stub('localhost', 50051) as stub:
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you', message='hey dude'), _TIMEOUT_SECONDS)
        print(response)


if __name__ == '__main__':
    run()
