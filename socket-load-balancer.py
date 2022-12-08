import socket
import threading
import random
import sys

full_path = '/home/mininet/Network-Load-Balancer-Simulation'

'''
Nothing but some book-keeping to load the server IP's of the different mininet hosts running server.py programs
on both the tree and star topologies
'''

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



'''
Round Robin algorithm
1) Lock to ensure integrity of the round robin index because of race conditions due to multiple clients
2) Index is needed to loop through the list of avaialble servers to distribute the load equally among them
'''
RoundRobin_index = 0
RR_index_lock = threading.Lock()
def RoundRobin(cur, choice):
	next = cur % len(choice)
	return choice[next]

'''
Pseudo random algorithm which just picks one of the available servers at random
'''
def Random(choice):
	next = random.randint(0, len(choice) - 1)
	return choice[next]

'''
Function to handle a client request
'''
def handle_request(conn, addr):
  global RoundRobin_index
  print('Connected by', addr)

  # Depending on if the topology is tree/star, the choice of server IP's will change
  choice_servers = []
  if (sys.argv[1] == 'star'):
    choice_servers = backend_servers_star_topo
  elif (sys.argv[1] == 'tree'):
    choice_servers = backend_servers_tree_topo

  # Depending on which algorithm keyword is passed as an argument, call those algorithms accordingly
  # Store which backend server mininet host should the client request go to in this variable
  next = None
  if (sys.argv[2] == 'RR'):
    # Acquire a lock for the RR index, as it might lead to race conditions with multiple clients using the balancer
    RR_index_lock.acquire(blocking=True)
    next = RoundRobin(cur=RoundRobin_index, choice=choice_servers)
    RR_index_lock.release()
  elif (sys.argv[2] == 'Random'):
    next = Random(choice=choice_servers)

  # Open a socket to connect to the HTTP server on the mininet host chosen by the algorithm
  # Since we only simulate GET requests, the HTTP format is not too hard to manipulate
  forward_packet_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  forward_packet_socket.connect((next, 8080))
  forward_packet_socket.send(f"GET / HTTP/1.1\r\nHost:{next}\r\nConnection: close\r\n\r\n".encode())
  
  
  # Collecting the response from the backend server chosen by the balancing algorithm
  # Using fixed BUFFER SIZE of 8192, instead of loading the response at once
  response = b""
  while True:
    chunk = forward_packet_socket.recv(8192)
    if len(chunk) == 0:
        break
    response = response + chunk
  
  # Close this socket as we have recieved the entire response from the server chosen by the specified algorithm
  forward_packet_socket.close()

  # Sending the response chunk back to the client from a server
  sent = 0
  while sent < len(response):
    sent = sent + conn.send(response[sent:])

  # Acquire a lock for the RR index, as it might lead to race conditions with multiple clients
  # trying to update the round robin index
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

'''
Entry point for our load balancer, socket is binded to a port
and on every client connection a new thread is spawned to handle the request
'''
while True:
  conn, addr = s.accept()
  thread = threading.Thread(target=handle_request, args=(conn, addr))
  thread.start()

