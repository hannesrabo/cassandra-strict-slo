import logging
import mock
import unittest
from cassandra.cassandra_host import CassandraHost


class TestCassandraHost(unittest.TestCase):
    """Test cassandra instance in the network."""

    def setUp(self):
        self.host = mock.MagicMock()
        self.cassandra_host = \
            CassandraHost(self.host,
                          "h1",
                          cluster_name="mininet-cassandra-cluster",
                          data_center="datacenter1",
                          max_heap="1024M",
                          core="0",
                          seed_nodes="111.111.111.111")

    def test_get_docker_name(self):
        self.assertEqual("cassandra-host-h1",
                         self.cassandra_host.get_docker_name())

    def test_start_cassandra_host(self):
        self.host.cmd = mock.MagicMock()

        self.cassandra_host.start_cassandra_host()

        self.host.cmd.assert_called_with(
            "docker run --name cassandra-host-h1 -p 9042:9042 "
            "-e CASSANDRA_CLUSTER_NAME=mininet-cassandra-cluster "
            "-e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch "
            "-e CASSANDRA_DC=datacenter1 -e HEAP_NEWSIZE=1M "
            "-e MAX_HEAP_SIZE=1024M "
            "--cpuset-cpus=\"0\" "
            "-e CASSANDRA_SEEDS=111.111.111.111 "
            "-d cassandra"
        )
