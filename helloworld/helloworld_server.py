#!/usr/local/bin/grun

import time

import helloworld_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class helloworld(helloworld_pb2.EarlyAdopterhelloworldServicer):

    def SayHello(self, request, context):
        print("request: " + str(request)) 
        return helloworld_pb2.HelloReply(message='%s, %s!' % (request.message, request.name))


def serve():
    server = helloworld_pb2.early_adopter_create_helloworld_server(
            helloworld(), 50051, None, None)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop()

if __name__ == '__main__':
    serve()
