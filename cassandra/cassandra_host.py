import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

docker_cmd_stop = "docker stop {name}"
docker_cmd_remove = "docker rm {name}"
docker_cmd_run = "docker run --name {name} {flags} -d cassandra"


class CassandraHost():
    """Represents a cassandra instance in the network."""

    def __init__(self,
                 topology,
                 name,
                 cluster_name="mininet-cassandra-cluster",
                 data_center="datacenter1",
                 max_heap="1024M",
                 core=None,
                 seed_node=None):
        """Container class for a cassandra host."""
        self.topology = topology
        self.name = name

        self.cluster_name = cluster_name
        self.data_center = data_center
        self.max_heap = max_heap

        # Represents which core in the system it should run on
        self.core = core

        # The IP of the seed node in the cluster
        self.seed_node = seed_node

    def get_host(self):
        """Return the host from the mininet topology"""
        return self.topology.getHost(self.name)

    def get_docker_name(self):
        """Get the name of the docker container that is running in this host"""
        return "cassandra-host-%s" % self.name

    def start_cassandra_host(self):
        """Starts a cassandra instance on this host."""
        flags = [
            "-p 9042:9042",
            "-e CASSANDRA_CLUSTER_NAME=%s" % self.cluster_name,
            "-e CASSANDRA_ENDPOINT_SNITCH=GossipingPropertyFileSnitch",
            "-e CASSANDRA_DC=%s" % self.data_center,
            "-e HEAP_NEWSIZE=1M",
            "-e MAX_HEAP_SIZE=%s" % self.max_heap,
        ]

        if self.core:
            flags.append(
                "--cpuset-cpus=\"%s\"" % self.core,
            )

        if self.seed_node:
            flags.append(
                "-e CASSANDRA_SEEDS=%s" % self.seed_node,
            )

        flags_str = " ".join(flags)

        # Make sure we don't have any old processes running in this name.
        host = self.get_host()

        host.cmd(docker_cmd_stop.format(name=self.get_docker_name()))
        host.cmd(docker_cmd_remove.format(name=self.get_docker_name()))

        # Start the new docker container.
        host.cmd(docker_cmd_run.format(
            name=self.get_docker_name(),
            flags=flags_str
        ))
