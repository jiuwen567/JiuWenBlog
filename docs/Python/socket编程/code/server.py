import socket
if __name__ == '__main__':
   tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   tcp_server.bind(("",8080)) #本机任意IP都可以，一般不指定
   tcp_server.listen(128)# 最大连接数
   result = tcp_server.accept() 
   print(result)
   connection,client_address = result #元组拆包
   print(connection)#新的套接字对象,收发消息不使用tcp_server，而是使用connection
   print(client_address)
   #阻塞等待客户端发送数据
   recv_data = connection.recv(1024)
   print(recv_data.decode('utf-8'))
   send_data = connection.send('服务端发来的数据'.encode('utf-8'))
   connection.close()#关闭服务套接字
   tcp_server.close()#关闭服务端套接字