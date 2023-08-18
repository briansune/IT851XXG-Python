import socket
import time

pld_ip = '192.168.1.212'
pld_port = 8085

pld_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def pld_status(cmd, sub):
    pld_socket.sendall('STAT:{}:{}?\n'.format(cmd, sub).encode('utf-8'))
    reply = pld_socket.recv(4096)
    if reply:
        b = reply.strip().decode()
        print(b)


try:
    pld_socket.connect((pld_ip, pld_port))
except socket.error:
    print('fail')

pld_socket.sendall(b'SYST:REM\n')
pld_socket.sendall(b'SYST:BEEP:IMM\n')

pld_socket.sendall(b'*IDN?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'*TST?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SYST:VERS?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SYST:SENS?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SYST:CHAN:NUMB?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'LINK:MODE?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'CHAN?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_status('QUES', 'EVEN')
pld_status('QUES', 'COND')
pld_status('QUES', 'ENAB')

pld_status('OPER', 'EVEN')
pld_status('OPER', 'ENAB')

pld_socket.sendall(b'INP:STAT?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SOUR:INP?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SOUR:INP:SHOR?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SOUR:FUNC?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SOUR:FUNC VOLT\n')

pld_socket.sendall(b'SOUR:FUNC?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SOUR:FUNC CURR\n')

pld_socket.sendall(b'SOUR:FUNC?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SOUR:FUNC:MODE?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SOUR:VOLT:RANG?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SOUR:VOLT:RANG:AUTO?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SOUR:POW:PROT?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SOUR:POW:CONF?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SOUR:CURR:RANG?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SOUR:CURR:RANG 5\n')

pld_socket.sendall(b'SOUR:CURR:SLEW:RISE?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SOUR:CURR:SLEW:FALL?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SOUR:CURR:SLEW:BOTH?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'SOUR:CURR:RANG?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'MEAS:VOLT?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'MEAS:VOLT:MAX?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'MEAS:VOLT:MIN?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'MEAS:CURR?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'MEAS:CURR:MAX?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'MEAS:CURR:MIN?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'MEAS:VOLT:RIPP?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)

pld_socket.sendall(b'MEAS:CURR:RIPP?\n')
reply = pld_socket.recv(4096)
if reply:
    b = reply.strip().decode()
    print(b)


pld_socket.sendall(b'SYST:LOC\n')

pld_socket.close()
