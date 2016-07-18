import socket

target_host = "www.yahoo.com"
target_port = 80

# cria um objeto socket
# socket.socket([family,[tipe[,proto]]]) 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# conecta o cliente

client.connect((target_host,target_port))


# envia data

client.send("GET / HTTP1.1\r\nHost: yahoo.com\r\n\r\n")

# recebe data

response = client.recv(4096)

print response
