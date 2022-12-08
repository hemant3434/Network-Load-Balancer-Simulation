import requests
import sys

'''
Very simple client script that sends 50 HTTP GET requests to the load balancer.
Writes the results to a log file in the data_capture directory whose name should
be specified by a command line argument
'''


num_req = 50
node_balancer_ip = "10.0.0.1"
node_balancer_port = 8081
full_path = '/home/mininet/Network-Load-Balancer-Simulation/data_capture'

for i in range(num_req):
  resp = requests.get(f'http://{node_balancer_ip}:{node_balancer_port}')
  # print(resp.text)
  # print(resp.elapsed.total_seconds())
  with open(f'{full_path}/{sys.argv[1]}-log.txt', 'a+') as log:
    log.write(str(resp.elapsed.total_seconds())+'\n')

