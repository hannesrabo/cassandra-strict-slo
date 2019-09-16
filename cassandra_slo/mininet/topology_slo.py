from mininet.node import OVSController
from time import sleep
from mininet.node import OVSSwitch
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.node import Switch
from mininet.net import Mininet
from mininet.topo import Topo
from cassandra_slo.cassandra.cassandra_host import CassandraHost


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
            cleanup=True
        )

        # Start the network
        self.net.start()

        # print "topology ready!"
        # Give some time for network to set up
        sleep(1)

        cassandra1_name = 'h1'
        self.cassandra1 = CassandraHost(
            self.getHost(cassandra1_name), cassandra1_name
        )
        self.cassandra1.start_cassandra_host()

        # Make sure that everything is set up
        sleep(1)

    def createTopology(self):
        # Initialize topology
        Topo.__init__(self)

        # Add the switch
        sw1 = self.addSwitch('s1')

        # Add hosts
        host1 = self.addHost('h1', ip="100.0.0.11/24")
        host2 = self.addHost('h2', ip="100.0.0.12/24")
        host3 = self.addHost('h3', ip="100.0.0.13/24")
        host4 = self.addHost('h4', ip="100.0.0.14/24")
        host5 = self.addHost('h5', ip="100.0.0.15/24")
        host6 = self.addHost('h6', ip="100.0.0.16/24")
        host7 = self.addHost('h7', ip="100.0.0.17/24")
        host8 = self.addHost('h8', ip="100.0.0.18/24")

        # Links
        self.addLink(host1, sw1)
        self.addLink(host2, sw1)
        self.addLink(host3, sw1)
        self.addLink(host4, sw1)
        self.addLink(host5, sw1)
        self.addLink(host6, sw1)
        self.addLink(host7, sw1)
        self.addLink(host8, sw1)

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
