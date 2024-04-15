from concurrent import futures
import os
import time
import mysql.connector
import grpc
import srv_pb2_grpc as pb2_grpc
import srv_pb2 as pb2
import uuid


conn = mysql.connector.connect(host="localhost", user="root", database="test")
cur = conn.cursor()


class SrvServicer(pb2_grpc.SrvServicer):
    def __init__(self, *args, **kwargs):
        pass

    def Ping(self, request: pb2.SimpleSrvRequest, context):
        time.sleep(3)
        return pb2.SimpleSrvRepsonse(message=str(uuid.uuid4()), status="OK")

    def DatabaseStressTest(self, request: pb2.SimpleSrvRequest, context):
        random_string = str(uuid.uuid4())
        statement = f'INSERT INTO test_table (name) VALUES ("${random_string}")'
        cur.execute(statement)
        print("done")
        return pb2.SimpleSrvRepsonse(message="Stress Test Successful", status="OK")

    def UploadFile(self, request_iterator, context):
        file_data = b""
        file_name = str(uuid.uuid4())
        for chunk in request_iterator:
            file_data += chunk.data

        with open(f"received/{file_name}.bin", "wb") as file:
            file.write(file_data)

        os.remove(f"received/{file_name}.bin")
        return pb2.SimpleSrvRepsonse(message="File Received Successfully.", status="OK")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1000))
    pb2_grpc.add_SrvServicer_to_server(SrvServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Starting server. Listening on port 50051")
    serve()
