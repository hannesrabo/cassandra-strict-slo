import logging
import mock
import unittest
from cassandra.cassandra_host import CassandraHost

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

docker_cmd_stop = "docker stop {name}"
docker_cmd_remove = "docker rm {name}"
docker_cmd_run = "docker run --name {name} {flags} -d cassandra"


class TestCassandraHost(unittest.TestCase):
    """Test cassandra instance in the network."""

    def setUp(self):
        self.topology = mock.MagicMock()
        self.cassandra_host = \
            CassandraHost(self.topology,
                          "h1",
                          cluster_name="mininet-cassandra-cluster",
                          data_center="datacenter1",
                          max_heap="1024M",
                          core="0",
                          seed_node="111.111.111.111")

    def test_get_docker_name(self):
        self.assertEqual("cassandra-host-h1",
                         self.cassandra_host.get_docker_name())

    def test_start_cassandra_host(self):
        host = mock.MagicMock()
        host.cmd = mock.MagicMock()
        self.cassandra_host.get_host = mock.MagicMock()
        self.cassandra_host.get_host.return_value = host

        self.cassandra_host.start_cassandra_host()

        host.cmd.assert_called_with(
            "docker run --name cassandra-host-h1 -p 9042:9042 "
            "-e CASSANDRA_CLUSTER_NAME=mininet-cassandra-cluster "
            "-e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch "
            "-e CASSANDRA_DC=datacenter1 -e HEAP_NEWSIZE=1M "
            "-e MAX_HEAP_SIZE=1024M "
            "--cpuset-cpus=\"0\" "
            "-e CASSANDRA_SEEDS=111.111.111.111 "
            "-d cassandra"
        )
