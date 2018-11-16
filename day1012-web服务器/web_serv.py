# -*- coding: utf-8 -*-

# @Author   : lws
# @Time     : 2018/10/12 13:41
# @describe :


import threading
import socket
import re

HTML_ROOT_DIR = './html'


def handle_client(cli):
    data = cli.recv(1024)
    print data

    request_lines = data.splitlines()
    # for line in request_lines:
    #     print(line)

    # 解析请求报文
    # 'GET / HTTP/1.1'
    request_start_line = request_lines[0]
    # 提取用户请求的文件名
    # print("*"*10)
    # print(request_start_line.decode("utf-8"))
    # 正在匹配 'GET / HTTP/1.1' 中/及后边的字符串
    file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)

    if "/" == file_name:
        file_name = "/index.html"

    try:
        file = open(HTML_ROOT_DIR + file_name, "rb")
    except IOError:
        response_start_line = "HTTP/1.1 404 Not Found\r\n"
        response_headers = "Server: My server\r\n"
        response_body = "The file is not found!"
    else:
        file_data = file.read()
        file.close()

        # 构造响应数据
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: My server\r\n"
        response_body = file_data.decode("utf-8")

    response = response_start_line + response_headers + "\r\n" + response_body
    print "response data:", response

    # 向客户端返回响应数据
    cli.send(response)

    # 关闭客户端连接
    cli.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ADDRESS = ('127.0.0.1', 55555)
    s.bind(ADDRESS)
    s.listen(10)
    print "服务开始启动....."

    while True:
        cli, addr = s.accept()
        p = threading.Thread(target=handle_client, args=(cli,))
        p.start()
        p.join()
        cli.close()
