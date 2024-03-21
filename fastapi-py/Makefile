start_server:
	uvicorn main:app --reload

loadtest:
	plow http://127.0.0.1:8000/ping -c 1000 -n 10000 
