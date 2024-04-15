start_server:
	uvicorn main:app --reload

loadtest_ping:
	plow -c 1000 -n 1000000 -d 3m http://localhost:8000/ping
	# wrk -c1000 -d1m http://localhost:8000/ping --latency

loadtest_file_upload:
	wrk -t8 -c1000 -d 3m -s request.lua http://localhost:8000/upload-file

