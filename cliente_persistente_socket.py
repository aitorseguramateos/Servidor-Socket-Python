import socket

# Definir la dirección IP y el puerto del servidor
SERVER_HOST = '192.168.80.129'  # Dirección IP del servidor
SERVER_PORT = 12345        # Puerto en el que el servidor está escuchando

# Crear un objeto de socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Conectar al servidor
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    
    print("Conexión establecida con el servidor.")
    
    # Loop para mantener la conexión persistente
    while True:
        # Enviar datos al servidor
        message = input("Ingrese un mensaje para enviar al servidor: ")
        client_socket.sendall(message.encode())
        
        # Recibir respuesta del servidor
        data = client_socket.recv(1024)
        print('Respuesta del servidor:', data.decode())
