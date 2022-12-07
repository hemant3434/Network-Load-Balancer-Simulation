import http.server
import socketserver
import sys
import random

full_path = '/home/mininet/Network-Load-Balancer-Simulation'

PORT = 8081


def RoundRobin(cur, choice):
	next = cur % len(choice)
	return choice[next]

def Random(choice):
	next = random.randint(0, len(choice) - 1)
	return choice[next]

backend_servers_star_topo = []
with open(f"{full_path}/backend_server_addrs_star_topo.txt", 'r') as addrs:
  for addr in addrs:
    backend_servers_star_topo.append(addr.strip())

backend_server_simple = []
with open(f"{full_path}/backend_server_simple.txt", 'r') as addrs:
  for addr in addrs:
    backend_server_simple.append(addr.strip())

print(f"Current backend/data servers for star topology: {backend_servers_star_topo}")

RoundRobin_index = 0

class MyHandler(http.server.SimpleHTTPRequestHandler):
  def do_GET(self):
    global RoundRobin_index
    choice_servers = []
    if (sys.argv[1] == 'star'):
      choice_servers = backend_servers_star_topo
    elif (sys.argv[1] == 'simple'):
      choice_servers = backend_server_simple

    next = None
    if (sys.argv[2] == 'RR'):
      next = RoundRobin(cur=RoundRobin_index, choice=choice_servers)
    elif (sys.argv[2] == 'Random'):
      next = Random(choice=choice_servers)

    RoundRobin_index = RoundRobin_index + 1
    
    self.send_response(301)
    self.send_header('Location', next)
    self.end_headers()

Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()