import socket
import threading
import random
import sys

full_path = '/home/mininet/Network-Load-Balancer-Simulation'

backend_servers_star_topo = []
with open(f"{full_path}/backend_server_addrs_star_topo.txt", 'r') as addrs:
  for addr in addrs:
    backend_servers_star_topo.append(addr.strip())

backend_servers_tree_topo = []
with open(f"{full_path}/backend_server_addrs_tree_topo.txt", 'r') as addrs:
  for addr in addrs:
    backend_servers_tree_topo.append(addr.strip())

print(f"Current backend/data servers for star topology: {backend_servers_star_topo}")
print(f"Current backend/data servers for tree topology: {backend_servers_tree_topo}")

RoundRobin_index = 0
RR_index_lock = threading.Lock()

def RoundRobin(cur, choice):
	next = cur % len(choice)
	return choice[next]

def Random(choice):
	next = random.randint(0, len(choice) - 1)
	return choice[next]

def handle_request(conn, addr):
  global RoundRobin_index
  print('Connected by', addr)

  choice_servers = []
  if (sys.argv[1] == 'star'):
    choice_servers = backend_servers_star_topo
  elif (sys.argv[1] == 'tree'):
    choice_servers = backend_servers_tree_topo

  next = None
  if (sys.argv[2] == 'RR'):
    RR_index_lock.acquire(blocking=True)
    next = RoundRobin(cur=RoundRobin_index, choice=choice_servers)
    RR_index_lock.release()
  elif (sys.argv[2] == 'Random'):
    next = Random(choice=choice_servers)

  forward_packet_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  forward_packet_socket.connect((next, 8080))
  forward_packet_socket.send(f"GET / HTTP/1.1\r\nHost:{next}\r\nConnection: close\r\n\r\n".encode())
  response = b""
  while True:
    chunk = forward_packet_socket.recv(8192)
    if len(chunk) == 0:
        break
    response = response + chunk
  forward_packet_socket.close()

  sent = 0
  while sent < len(response):
    sent = sent + conn.send(response[sent:])
  
  RR_index_lock.acquire(blocking=True)
  RoundRobin_index = RoundRobin_index + 1
  RR_index_lock.release()

  conn.close()

host = ''
PORT = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, PORT))
print(f"Server started on port {PORT}, ip {socket.gethostbyname(socket.gethostname())}")
s.listen()

while True:
  conn, addr = s.accept()
  thread = threading.Thread(target=handle_request, args=(conn, addr))
  thread.start()

