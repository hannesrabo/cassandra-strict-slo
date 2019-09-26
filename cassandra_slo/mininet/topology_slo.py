from mininet.node import OVSController
from time import sleep
from mininet.node import OVSSwitch
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.link import TCLink

#For Core Pinning
from mininet.node import Switch, CPULimitedHost
from mininet.util import numCores


cassandra_node_1 = 'h1'
cassandra_node_2 = 'h2'
cassandra_node_3 = 'h3'
cassandra_node_4 = 'h4'

cassandra_ip_1 = '100.0.0.11'
cassandra_ip_2 = '100.0.0.12'
cassandra_ip_3 = '100.0.0.13'
cassandra_ip_4 = '100.0.0.14'

cassandra_private_dirs = [('/slo/cassandra', '/slo/cassandra/%(name)s')]


class MyTopo(Topo):
    "Simple topology example."

    def __init__(self):
        "Create custom topology."
        self.createTopology()

        # Create network
        self.net = Mininet(
            topo=self,
            switch=OVSSwitch,
            controller=OVSController,
            autoSetMacs=True,
            autoStaticArp=True,
            build=True,
            cleanup=True,
            link=TCLink,
            autoPinCpus=True,       #added parameter for core pinning
            host=CPULimitedHost     #added parameter for core pinning
        )

        # Start the network
        self.net.start()

        # print "topology ready!"
        # Give some time for network to set up
        sleep(1)

        self.startCassandra('h1')
        self.startCassandra('h2')

    # TESTING CORE PINNING (returns number of cores)
	numOfCores = numCores()
	print 'The number of cores is: ', numOfCores

    # Assign cores to the hosts
	self.getHost('h1').config(cores=1)	
	self.getHost('h2').config(cores=0)	
	self.getHost('h3').config(cores=2)	
	self.getHost('h4').config(cores=3)	
	self.getHost('h5').config(cores=4)	
	self.getHost('h6').config(cores=5)	

        # Make sure that everything is set up
        sleep(1)

    

    def createTopology(self):
        # Initialize topology
        Topo.__init__(self)

        # Add the switch
        sw1 = self.addSwitch('s1')

        # Add hosts
        host1 = self.addHost('h1', ip="100.0.0.11/24",
                             privateDirs=cassandra_private_dirs)
        host2 = self.addHost('h2', ip="100.0.0.12/24",
                             privateDirs=cassandra_private_dirs)
        host3 = self.addHost('h3', ip="100.0.0.13/24",
                             privateDirs=cassandra_private_dirs)
        host4 = self.addHost('h4', ip="100.0.0.14/24",
                             privateDirs=cassandra_private_dirs)
        host5 = self.addHost('h5', ip="100.0.0.15/24",
                             privateDirs=cassandra_private_dirs)
        host6 = self.addHost('h6', ip="100.0.0.16/24",
                             privateDirs=cassandra_private_dirs)
        
        # Links
        self.addLink(host1, sw1, delay="0.1ms")
        self.addLink(host2, sw1, delay="0.1ms")
        self.addLink(host3, sw1, delay="0.1ms")
        self.addLink(host4, sw1, delay="0.1ms")
        self.addLink(host5, sw1, delay="0.1ms")
        self.addLink(host6, sw1, delay="0.1ms")

    def getNet(self):
        return self.net

    def getHost(self, name):
        return self.net.get(name)

    def startCassandra(self, name):
        host = self.getHost(name)
        host.cmd('./tools/start-cassandra.sh &')

    def enableCLI(self):
        CLI(self.net)


if __name__ == "__main__":
    # Create UC Topology instance
    topo = MyTopo()
    CLI(topo.getNet())

