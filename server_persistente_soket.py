import socket

# Definir la dirección IP y el puerto en el que el servidor estará escuchando
HOST = '192.168.80.129'  # Dirección IP local
PORT = 12345        # Puerto no privilegiado (> 1023)

# Crear un objeto de socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Permitir reutilizar la dirección IP y puerto
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Enlazar el socket al HOST y al PUERTO
    server_socket.bind((HOST, PORT))
    
    # Escuchar conexiones entrantes (máximo 1)
    server_socket.listen(1)
    
    print("Servidor de socket iniciado. Esperando conexiones...")
    
    # Loop principal para aceptar conexiones continuamente
    while True:
        # Aceptar una conexión entrante
        conn, addr = server_socket.accept()
        print('Conexión establecida con', addr)
        
        # Loop para manejar la conexión
        while True:
            # Recibir datos del cliente
            data = conn.recv(1024)
            if not data:
                break
            
            print('Mensaje recibido:', data.decode())
            
            # Responder al cliente
            conn.sendall(b'Mensaje recibido por el servidor.')
        
        # Cerrar la conexión una vez que el cliente se desconecta
        conn.close()