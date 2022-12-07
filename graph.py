import matplotlib.pyplot as plt

full_path='/home/mininet/Network-Load-Balancer-Simulation/data_capture'

def helper(list_of_file_names):
  data_files = list_of_file_names

  c1_f = open(f'{full_path}/{data_files[0]}')
  c2_f = open(f'{full_path}/{data_files[1]}')
  c3_f = open(f'{full_path}/{data_files[2]}')

  c1_data = [ (float(i.strip()) * 1000) for i in c1_f.readlines()]
  c2_data = [ (float(i.strip()) * 1000) for i in c2_f.readlines()]
  c3_data = [ (float(i.strip()) * 1000) for i in c3_f.readlines()]

  final_data = []
  for i in range(0, len(c1_data)):
    final_data.append((c1_data[i] + c2_data[i] + c3_data[i]) / 3)

  c1_f.close()
  c2_f.close()
  c3_f.close()

  return final_data

def graph_star_topology():
  random = helper(['client-1-star-random-log.txt', 'client-2-star-random-log.txt', 'client-3-star-random-log.txt'])
  round_robin = helper(['client-1-star-RR-log.txt', 'client-2-star-RR-log.txt', 'client-3-star-RR-log.txt'])
  
  plt.plot(random, label = "random")
  plt.plot(round_robin, label = "round robin")
  plt.show()

# def graph_star_round_robin():
#   data_files = ['client-1-star-RR-log.txt', 'client-2-star-RR-log.txt', 'client-3-star-RR-log.txt']

graph_star_topology()