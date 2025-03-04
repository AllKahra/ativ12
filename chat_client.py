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
HOST = config.get('host', '127.0.0.1')
PORT = int(config.get('port', 12345))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = input("Você: ")
    client_socket.send(message.encode('utf-8'))

    if message.lower() == 'sair':
        print("Conexão encerrada pelo cliente.")
        break

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Servidor: {response}")

client_socket.close()
