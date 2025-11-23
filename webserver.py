# Importa o módulo socket
from socket import *
import sys # Necessário para encerrar o programa [cite: 19]

# Cria o socket TCP (orientado à conexão) [cite: 20]
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepara o socket do servidor
#Fill in start
serverPort = 6789 # Porta sugerida para teste [cite: 56, 59]
serverSocket.bind(('', serverPort)) # Associa o socket ao IP da máquina local e à porta
serverSocket.listen(1) # O servidor escutará por no máximo 1 conexão por vez
#Fill in end

while True:
    # Estabelece a conexão [cite: 26]
    print('Ready to serve...')
    #Fill in start
    connectionSocket, addr = serverSocket.accept() # Aceita a conexão de um cliente (navegador) [cite: 4]
    #Fill in end
    
    try:
        # Recebe a mensagem do cliente (requisição HTTP) [cite: 5]
        #Fill in start
        message = connectionSocket.recv(1024).decode() # Recebe os dados e decodifica para string
        #Fill in end
        
        # Analisa a requisição para obter o nome do arquivo [cite: 5]
        filename = message.split()[1]
        f = open(filename[1:]) # Abre o arquivo solicitado (removendo a barra '/' inicial)
        
        # Obtém o conteúdo do arquivo [cite: 6]
        #Fill in start
        outputdata = f.read() # Lê o conteúdo do arquivo no sistema de arquivos do servidor
        #Fill in end
        
        # Cria e Envia a linha de status do cabeçalho HTTP (200 OK) [cite: 7]
        #Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) # Linha de status e linha vazia para separar cabeçalho do conteúdo
        #Fill in end
        
        # Envia o conteúdo do arquivo ao cliente [cite: 8]
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        
        connectionSocket.send("\r\n".encode())
        
        # Fecha a conexão com o cliente [cite: 42]
        connectionSocket.close()
        
    except IOError: # Captura o erro se o arquivo não for encontrado (ex: "FileNotFoundError" em Python)
        # Envia mensagem de erro 404 se o arquivo não for encontrado [cite: 9]
        #Fill in start
        error_response = "HTTP/1.1 404 Not Found\r\n\r\n<h1>404 Not Found</h1>"
        connectionSocket.send(error_response.encode())
        #Fill in end
        
        # Fecha o socket do cliente [cite: 48]
        #Fill in start
        connectionSocket.close()
        #Fill in end

# serverSocket.close() # Fechamento do socket principal fora do loop
# sys.exit() # Encerra o programa [cite: 52]