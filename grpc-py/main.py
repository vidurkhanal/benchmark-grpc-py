from concurrent import futures
import grpc
import srv_pb2_grpc as pb2_grpc
import srv_pb2 as pb2


class SrvServicer(pb2_grpc.SrvServicer):
    def __init__(self, *args, **kwargs):
        pass

    def Ping(self, request: pb2.SimpleSrvRequest, context):
        return pb2.SimpleSrvRepsonse(message="Pong", status="OK")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_SrvServicer_to_server(SrvServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Starting server. Listening on port 50051")
    serve()
