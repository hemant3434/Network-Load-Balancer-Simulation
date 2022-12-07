import requests
import sys

num_req = 100
node_balancer_ip = "10.0.0.1"
node_balancer_port = 8081
full_path = '/home/mininet/Network-Load-Balancer-Simulation/data_capture'

for i in range(num_req):
  resp = requests.get(f'http://{node_balancer_ip}:{node_balancer_port}')
  # print(resp.text)
  # print(resp.elapsed.total_seconds())
  with open(f'{full_path}/{sys.argv[1]}-log.txt', 'a+') as log:
    log.write(str(resp.elapsed.total_seconds())+'\n')



