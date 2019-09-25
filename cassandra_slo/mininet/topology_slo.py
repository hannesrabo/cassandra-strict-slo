from mininet.node import OVSController
from time import sleep
from mininet.node import OVSSwitch
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.node import Switch, CPULimitedHost
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.link import TCLink

# TESTING CORE PINNING
from mininet.util import numCores

from cassandra_slo.cassandra.cassandra_host import CassandraHost

cassandra_node_1 = 'h1'
cassandra_node_2 = 'h2'
cassandra_node_3 = 'h3'
cassandra_node_4 = 'h4'

cassandra_ip_1 = '100.0.0.11'
cassandra_ip_2 = '100.0.0.12'
cassandra_ip_3 = '100.0.0.13'
cassandra_ip_4 = '100.0.0.14'


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
	    autoPinCpus=True,
	    host=CPULimitedHost
        )

        # Start the network
        self.net.start()

        # print "topology ready!"
        # Give some time for network to set up
        sleep(1)

# TESTING CORE PINNING
	numOfCores = numCores()
	print 'The number of cores is: ', numOfCores

#        self.cassandra1 = CassandraHost(
#            host=self.getHost(cassandra_node_1),
#            name=cassandra_node_1,
#            core=0,
#            seed_nodes="%s,%s" % (cassandra_ip_1, cassandra_ip_2),
#        )
#        self.cassandra2 = CassandraHost(
#            host=self.getHost(cassandra_node_2),
#            name=cassandra_node_2,
#            core=1,
#            seed_nodes="%s,%s" % (cassandra_ip_1, cassandra_ip_2),
#        )
#        self.cassandra3 = CassandraHost(
#            host=self.getHost(cassandra_node_3),
#            name=cassandra_node_3,
#            core=2,
#            seed_nodes="%s,%s" % (cassandra_ip_1, cassandra_ip_2),
#        )
#        self.cassandra4 = CassandraHost(
#            host=self.getHost(cassandra_node_4),
#            name=cassandra_node_4,
#            core=3,
#            seed_nodes="%s,%s" % (cassandra_ip_1, cassandra_ip_2),
#        )
#
#        # Starting seeds nodes.
#        self.cassandra1.start_cassandra_host()
#        self.cassandra2.start_cassandra_host()
#
#        sleep(5)
#
#        # Starting the rest of the nodes.
#        self.cassandra3.start_cassandra_host()
#        self.cassandra4.start_cassandra_host()
#
#        # Make sure that everything is set up
#        sleep(1)
#
    def createTopology(self):
        # Initialize topology
        Topo.__init__(self)

        # Add the switch
        sw1 = self.addSwitch('s1')

        # Add hosts
        host1 = self.addHost('h1', ip="100.0.0.11/24")
	host1.config(cores=1)
        host2 = self.addHost('h2', ip="100.0.0.12/24")
        host3 = self.addHost('h3', ip="100.0.0.13/24")
        host4 = self.addHost('h4', ip="100.0.0.14/24")
        host5 = self.addHost('h5', ip="100.0.0.15/24")
#        host6 = self.addHost('h6', ip="100.0.0.16/24")
#        host7 = self.addHost('h7', ip="100.0.0.17/24")
#        host8 = self.addHost('h8', ip="100.0.0.18/24")

        # Links
        self.addLink(host1, sw1, delay="0.1ms")
        self.addLink(host2, sw1, delay="0.1ms")
        self.addLink(host3, sw1, delay="0.1ms")
        self.addLink(host4, sw1, delay="0.1ms")
        self.addLink(host5, sw1, delay="0.1ms")
#        self.addLink(host6, sw1, delay="0.1ms")
#        self.addLink(host7, sw1, delay="0.1ms")
#        self.addLink(host8, sw1, delay="0.1ms")

    def getNet(self):
        return self.net

    def getHost(self, name):
        return self.net.get(name)

    #     def startHTTP(self, name):
    #         host = self.getHost(name)
    #         host.cmd('python application/web/http_server.py ' + name + ' &')

    def enableCLI(self):
        CLI(self.net)


if __name__ == "__main__":
    # Create UC Topology instance
    topo = MyTopo()
    CLI(topo.getNet())
