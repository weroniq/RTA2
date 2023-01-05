# 1. Socket pyspark receiver
run the program socket_producer.py for example:
```bash
python socket_producer.py
```

# 2. Socket pyspark receiver
```bash
cd socket_receiver
docker build --tag wb72698/socket_receiver:latest .
docker run -d --rm --name my_socket_receiver wb72698/socket_receiver:latest
cd ..
```
