import grpc
import carro_pb2
import carro_pb2_grpc

def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = carro_pb2_grpc.CarroServiceStub(channel)

    placa_input = input(str("Digite a placa do carro: "))
    renavan_input = input(str("Digite o renavan do carro: "))
    request = carro_pb2.CarroRequest(placa=placa_input, renavan=renavan_input)
    response = stub.calcularValorTotal(request)
    print("Código de barras:", response.codigo_barras)
    print("Valor total:", response.valor_total)



if __name__ == '__main__':
    main()
