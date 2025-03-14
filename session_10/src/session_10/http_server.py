import socket
import logging

# Configura o logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define o host e a porta para escutar as conexões
HOST, PORT = '127.0.0.1', 8080

# Cria um socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Permite a reutilização imediata do endereço após a saída do programa
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Associa o socket ao host e à porta
    server_socket.bind((HOST, PORT))
    # Escuta por conexões entrantes
    server_socket.listen(1)
    logging.info(f"A servir HTTP em {HOST} na porta {PORT} ...")

    while True:
        # Aceita uma nova conexão de cliente
        client_connection, client_address = server_socket.accept()
        with client_connection:
            logging.info(f"Nova conexão de {client_address}")
            
            # Recebe os dados da requisição (limita a 1024 bytes por simplicidade)
            request_data = client_connection.recv(1024).decode('utf-8')
            logging.debug(f"Requisição recebida:\n{request_data}")

            # Processa a requisição (extrai o método e o caminho)
            try:
                method, path, _ = request_data.split("\r\n")[0].split()
                logging.info(f"Método HTTP: {method}")
                logging.info(f"Caminho solicitado: {path}")
            except ValueError as e:
                logging.error("Erro ao processar a requisição: formato inválido")
                method, path = 'GET', '/'

            # Constrói uma resposta HTTP simples
            if path == '/':
                http_response = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/html; charset=utf-8\r\n"
                    "Content-Length: 46\r\n"
                    "\r\n"
                    "<html><body><h1>Helloo, HTTP!</h1></body></html>"
                )
                logging.info("Resposta: 200 OK para '/'")
            elif path == '/about':
                http_response = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/html; charset=utf-8\r\n"
                    "Content-Length: 46\r\n"
                    "\r\n"
                    "<html><body><h1>About!</h1></body></html>"
                )
                logging.info("Resposta: 200 OK para '/about'")
            else:
                http_response = (
                    "HTTP/1.1 404 Not Found\r\n"
                    "Content-Type: text/html; charset=utf-8\r\n"
                    "Content-Length: 46\r\n"
                    "\r\n"
                    "<html><body><h1>404 file not found!</h1></body></html>"
                )
                logging.warning(f"Recurso não encontrado: {path}")
            
            # Envia a resposta HTTP de volta para o cliente
            client_connection.sendall(http_response.encode('utf-8'))
            logging.info(f"Resposta enviada para {client_address}")
