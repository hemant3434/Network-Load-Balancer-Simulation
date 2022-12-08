echo " Deleting data captures for topologies --------------------------------- \n"
yes y | rm -f ./data_capture/**

echo " Running STAR Topology simulations --------------------------------- \n"
sudo mn -c > /dev/null 2>&1
echo " Running STAR Topology - 3 clients, 3 servers, 1 load balancer running random balancing algorithm\n"
sudo python3 ./topos/star-topology.py random > /dev/null 2>&1
echo " Running STAR Topology - 3 clients, 3 servers, 1 load balancer running round robin balancing algorithm\n"
sudo mn -c > /dev/null 2>&1
sudo python3 ./topos/star-topology.py round-robin > /dev/null 2>&1

echo " Running TREE Topology simulations --------------------------------- \n"
sudo mn -c > /dev/null 2>&1
echo " Running TREE Topology - 6 clients, 3 servers, 1 load balancer running random balancing algorithm\n"
sudo python3 ./topos/tree-topology.py random > /dev/null 2>&1
echo " Running TREE Topology - 6 clients, 3 servers, 1 load balancer running round robin balancing algorithm\n"
sudo mn -c > /dev/null 2>&1
sudo python3 ./topos/tree-topology.py round-robin > /dev/null 2>&1