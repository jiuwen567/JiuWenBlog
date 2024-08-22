import socket

if __name__ == '__main__':
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET:IPV4
    tcp_client.connect(("127.0.0.1",8888))#IP 端口
    send_data = 'Hello,我是客户端'
    tcp_client.send(send_data.encode('utf-8'))
    #阻塞等待服务端发送数据
    recv_data = tcp_client.recv(1024).decode('utf-8')#每次收到的最大字节数
    print(recv_data)
    tcp_client.close()