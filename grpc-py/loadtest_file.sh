#!/bin/sh
data=`base64 -i sample_file`

ghz --insecure \--proto ./protos/srv.proto -n 10000 -c 1000 --call protos.Srv.UploadFile 0.0.0.0:50051 --data '{"data": "'$data'"}'



