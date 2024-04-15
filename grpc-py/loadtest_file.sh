#!/bin/sh
data=`base64 -i sample_file`

ghz --insecure \--proto ./protos/srv.proto -n 1000000 -c 1000 -z 3m --timeout 0  --call protos.Srv.UploadFile 0.0.0.0:50051 --data '{"data": "'$data'"}'



