from socket import *
def connection_scan(tgt_host,tgt_port):
    try:
        connection_socket = socket(AF_INET, SOCK_STREAM)
        connection_socket.connect((tgt_host,tgt_port))
        print('[+]%d/tcp open'% tgt_port)
        connection_socket.close()
    except:
        print('[-]%d/tcp closed'% tgt_port)

def port_scan(tgt_host, tgt_ports):
    try:
        tgt_ip = gethostbyname(tgt_host)
    except:
        print('[-] Cannot resolve %s'% tgt_host)
        return
    try:
        tgt_name = gethostbyaddr(tgt_ip)
        print('[+] Scan resolved of: %s' % tgt_name[0])
    except:
        print('[+] Scan resolved of: %s'% tgt_ip)
    setdefaulttimeout(1)
    for tgt_port in tgt_ports:
        print('Scanning port: %d '% tgt_port)
        connection_scan(tgt_host, int(tgt_port))

port_scan('google.com', [80,22])