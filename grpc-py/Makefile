gen_grpc_stubs: 
	python3 -m grpc_tools.protoc --proto_path=./protos/ --python_out=. --grpc_python_out=. --pyi_out=. ./protos/srv.proto

clean_grpc_stubs:
	rm *_pb2*.*

# load testing using ghz, n = number of connections, c = number of concurrent connections
loadtest_ping:
	 ghz --insecure \--proto ./protos/srv.proto -n 1000000 -c 1000 -z 3m --call protos.Srv.Ping 0.0.0.0:50051 --timeout 0

loadtest_file_upload:
	sudo ./loadtest_file.sh
		
loadtest_database_stress:
	 ghz --insecure \--proto ./protos/srv.proto -n 1000 -c 10 --call protos.Srv.DatabaseStressTest 0.0.0.0:50051
