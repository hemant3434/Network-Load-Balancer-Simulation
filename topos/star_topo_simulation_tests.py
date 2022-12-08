import time
full_path='/home/mininet/Network-Load-Balancer-Simulation'

backend_server = "python3 " + full_path + '/server.py &'
def test_simple(mininet):
  mininet.get("h5").sendCmd(backend_server)

  mininet.get("h1").sendCmd("python3 " + full_path + '/server-load-balance.py simple Random &')

  mininet.get("h2").cmd("python3 " + full_path + '/client.py simple')

  time.sleep(20)
  return

def random_load_balancing(mininet):
  mininet.get("h5").sendCmd(backend_server)
  mininet.get("h6").sendCmd(backend_server)
  mininet.get("h7").sendCmd(backend_server)

  mininet.get("h1").sendCmd("python3 " + full_path + '/server-load-balance.py star Random &')

  mininet.get("h2").sendCmd("python3 " + full_path + '/client.py client-1-star-random &')
  mininet.get("h3").sendCmd("python3 " + full_path + '/client.py client-2-star-random &')
  mininet.get("h4").cmd("python3 " + full_path + '/client.py client-3-star-random')

  print("Finished now")

  time.sleep(20)
  return

def rr_load_balancing(mininet):
  mininet.get("h5").sendCmd(backend_server)
  mininet.get("h6").sendCmd(backend_server)
  mininet.get("h7").sendCmd(backend_server)

  mininet.get("h1").sendCmd("python3 " + full_path + '/server-load-balance.py star RR &')

  mininet.get("h2").sendCmd("python3 " + full_path + '/client.py client-1-star-RR &')
  mininet.get("h3").sendCmd("python3 " + full_path + '/client.py client-2-star-RR &')
  mininet.get("h4").cmd("python3 " + full_path + '/client.py client-3-star-RR')

  print("Finished now")

  time.sleep(20)
  return