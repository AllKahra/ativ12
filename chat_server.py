import socket
import sys

def load_config():
    config = {}
    try:
        with open('config.txt', 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                config[key] = value
    except Exception as e:
        print(f"Erro ao ler o arquivo de configuração: {e}")
        sys.exit(1)
    
    return config

config = load_config()
HOST = config.get('host', '172.16.38.50')
PORT = int(config.get('port', 12345))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Servidor aguardando conexões em {HOST}:{PORT}...")

client_socket, client_address = server_socket.accept()
print(f"Conexão estabelecida com {client_address}")

while True:
    message = client_socket.recv(1024).decode('utf-8')
    if message.lower() == 'sair':
        print("Conexão encerrada pelo cliente.")
        break
    print(f"Cliente: {message}")

    response = input("Você: ")
    client_socket.send(response.encode('utf-8'))
    if response.lower() == 'sair':
        print("Conexão encerrada pelo servidor.")
        break

client_socket.close()
server_socket.close()
