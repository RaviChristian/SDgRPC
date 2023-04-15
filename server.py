from concurrent import futures
import grpc
import carro_pb2
import carro_pb2_grpc
import random

import random

def gerar_numero_aleatorio():
    return random.randrange(10001)

def gerar_codigo_barras_aleatorio():
    codigo_barras = ""
    for i in range(13):
        codigo_barras += str(random.randint(0, 9))
    return codigo_barras


class CarroServer(carro_pb2_grpc.CarroServiceServicer):
    def calcularValorTotal(self, request, context):
        codigo_barras = gerar_codigo_barras_aleatorio()
        valor_total = gerar_numero_aleatorio()
        return carro_pb2.CarroResponse(codigo_barras=codigo_barras, valor_total=valor_total)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
carro_pb2_grpc.add_CarroServiceServicer_to_server(CarroServer(), server)
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
