import time
full_path='/home/mininet/Network-Load-Balancer-Simulation'

def test_simple(mininet):
  mininet.get("h5").sendCmd("python3 -m http.server 8080 &")

  mininet.get("h1").sendCmd("python3 " + full_path + '/server-load-balance.py simple Random &')

  mininet.get("h2").cmd("python3 " + full_path + '/client.py simple')

  time.sleep(10)
  return

def random_load_balancing(mininet):
  mininet.get("h5").sendCmd("python3 -m http.server 8080 &")
  mininet.get("h6").sendCmd("python3 -m http.server 8080 &")
  mininet.get("h7").sendCmd("python3 -m http.server 8080 &")

  mininet.get("h1").sendCmd("python3 " + full_path + '/server-load-balance.py star Random &')

  mininet.get("h2").sendCmd("python3 " + full_path + '/client.py client-1-star-random &')
  mininet.get("h3").sendCmd("python3 " + full_path + '/client.py client-2-star-random &')
  mininet.get("h4").cmd("python3 " + full_path + '/client.py client-3-star-random')

  time.sleep(30)
  return

def rr_load_balancing(mininet):
  mininet.get("h5").sendCmd("python3 -m http.server 8080 &")
  mininet.get("h6").sendCmd("python3 -m http.server 8080 &")
  mininet.get("h7").sendCmd("python3 -m http.server 8080 &")

  mininet.get("h1").sendCmd("python3 " + full_path + '/server-load-balance.py star RR &')

  mininet.get("h2").sendCmd("python3 " + full_path + '/client.py client-1-star-RR &')
  mininet.get("h3").sendCmd("python3 " + full_path + '/client.py client-2-star-RR &')
  mininet.get("h4").cmd("python3 " + full_path + '/client.py client-3-star-RR')

  time.sleep(30)
  return