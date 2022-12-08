import matplotlib.pyplot as plt

full_path='/home/mininet/Network-Load-Balancer-Simulation/data_capture'

def helper_star_topology(list_of_file_names):
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

def helper_graph_topology(list_of_file_names):
  data_files = list_of_file_names

  c1_f = open(f'{full_path}/{data_files[0]}')
  c2_f = open(f'{full_path}/{data_files[1]}')
  c3_f = open(f'{full_path}/{data_files[2]}')
  c4_f = open(f'{full_path}/{data_files[3]}')
  c5_f = open(f'{full_path}/{data_files[4]}')
  c6_f = open(f'{full_path}/{data_files[5]}')

  c1_data = [ (float(i.strip()) * 1000) for i in c1_f.readlines()]
  c2_data = [ (float(i.strip()) * 1000) for i in c2_f.readlines()]
  c3_data = [ (float(i.strip()) * 1000) for i in c3_f.readlines()]
  c4_data = [ (float(i.strip()) * 1000) for i in c4_f.readlines()]
  c5_data = [ (float(i.strip()) * 1000) for i in c5_f.readlines()]
  c6_data = [ (float(i.strip()) * 1000) for i in c6_f.readlines()]

  final_data = []
  for i in range(0, len(c1_data)):
    final_data.append((c1_data[i] + c2_data[i] + c3_data[i] + c4_data[i] + c5_data[i] + c6_data[i]) / 6)

  c1_f.close()
  c2_f.close()
  c3_f.close()
  c4_f.close()
  c5_f.close()
  c6_f.close()

  return final_data

def graph_star_topology():
  random = helper_star_topology(['client-1-star-random-log.txt', 'client-2-star-random-log.txt', 'client-3-star-random-log.txt'])
  round_robin = helper_star_topology(['client-1-star-RR-log.txt', 'client-2-star-RR-log.txt', 'client-3-star-RR-log.txt'])
  num_points = 50
  x_axis = [i for i in range(1, num_points+1)]

  plt.plot(x_axis, random, label="random")
  plt.plot(x_axis, round_robin, label="round robin")

  plt.xlabel("Request Number")
  plt.ylabel("Average RTT (ms)")
  plt.legend(loc='best')
  plt.axis([0, 50, 0, 50])

  plt.show()

def graph_tree_topology():
  random = helper_graph_topology(['client-1-tree-random-log.txt', 'client-2-tree-random-log.txt', 'client-3-tree-random-log.txt', 'client-4-tree-random-log.txt', 'client-5-tree-random-log.txt', 'client-6-tree-random-log.txt'])
  round_robin = helper_graph_topology(['client-1-tree-RR-log.txt', 'client-2-tree-RR-log.txt', 'client-3-tree-RR-log.txt', 'client-4-tree-RR-log.txt', 'client-5-tree-RR-log.txt', 'client-6-tree-RR-log.txt',])
  num_points = 50
  x_axis = [i for i in range(1, num_points+1)]

  plt.plot(x_axis, random, label="random")
  plt.plot(x_axis, round_robin, label="round robin")

  plt.xlabel("Request Number")
  plt.ylabel("Average RTT (ms)")
  plt.legend(loc='best')
  plt.axis([0, 50, 0, 200])

  plt.show()

graph_star_topology()
# graph_tree_topology()