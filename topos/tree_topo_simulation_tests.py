import time
full_path='/home/mininet/Network-Load-Balancer-Simulation'

backend_server = "python3 " + full_path + '/server.py &'
def random_load_balancing(mininet):
  mininet.get("h7").sendCmd(backend_server)
  mininet.get("h8").sendCmd(backend_server)
  mininet.get("h9").sendCmd(backend_server)

  mininet.get("h1").sendCmd("python3 " + full_path + '/server-load-balance.py tree Random &')

  mininet.get("h2").sendCmd("python3 " + full_path + '/client.py client-1-tree-random &')
  mininet.get("h3").sendCmd("python3 " + full_path + '/client.py client-2-tree-random &')
  mininet.get("h10").sendCmd("python3 " + full_path + '/client.py client-3-tree-random &')
  mininet.get("h4").sendCmd("python3 " + full_path + '/client.py client-4-tree-random &')
  mininet.get("h5").sendCmd("python3 " + full_path + '/client.py client-5-tree-random &')
  mininet.get("h6").cmd("python3 " + full_path + '/client.py client-6-tree-random')

  print("Finished now")

  time.sleep(20)
  return

def rr_load_balancing(mininet):
  mininet.get("h7").sendCmd(backend_server)
  mininet.get("h8").sendCmd(backend_server)
  mininet.get("h9").sendCmd(backend_server)

  mininet.get("h1").sendCmd("python3 " + full_path + '/server-load-balance.py tree RR &')

  mininet.get("h2").sendCmd("python3 " + full_path + '/client.py client-1-tree-RR &')
  mininet.get("h3").sendCmd("python3 " + full_path + '/client.py client-2-tree-RR &')
  mininet.get("h10").sendCmd("python3 " + full_path + '/client.py client-3-tree-RR &')
  mininet.get("h4").sendCmd("python3 " + full_path + '/client.py client-4-tree-RR &')
  mininet.get("h5").sendCmd("python3 " + full_path + '/client.py client-5-tree-RR &')
  mininet.get("h6").cmd("python3 " + full_path + '/client.py client-6-tree-RR')

  print("Finished now")
  time.sleep(20)
  return