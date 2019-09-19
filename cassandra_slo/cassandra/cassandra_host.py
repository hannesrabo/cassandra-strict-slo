import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

docker_cmd_stop = "docker stop {name}"
docker_cmd_remove = "docker rm {name}"
docker_cmd_run = "docker run --name {name} {flags} -d cassandra"


class CassandraHost():
    """Represents a Cassandra instance in the network."""

    def __init__(self,
                 host,
                 name,
                 cluster_name="mininet-cassandra-cluster",
                 data_center="datacenter1",
                 max_heap="1024M",
                 core=None,
                 seed_nodes=None):
        """Container class for a Cassandra host."""
        self.host = host
        self.name = name

        self.cluster_name = cluster_name
        self.data_center = data_center
        self.max_heap = max_heap

        # Represents which core in the system it should run on
        self.core = core

        # The IP of the seed nodes in the cluster
        self.seed_nodes = seed_nodes

    def get_docker_name(self):
        """Get the name of the docker container that is running in this host"""
        return "cassandra-host-%s" % self.name

    def start_cassandra_host(self):
        """Starts a cassandra instance on this host."""
        flags = [
            "--network=host",
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

        if self.seed_nodes:
            flags.append(
                "-e CASSANDRA_SEEDS=\"%s\"" % self.seed_nodes,
            )

        flags_str = " ".join(flags)

        # Make sure we don't have any old processes running in this name.
        self.host.cmd(docker_cmd_stop.format(name=self.get_docker_name()))
        self.host.cmd(docker_cmd_remove.format(name=self.get_docker_name()))

        cmd_string = docker_cmd_run.format(
            name=self.get_docker_name(),
            flags=flags_str
        )

        print(
            "Starting node: {name}\nCMD: {cmd}"
            .format(
                name=self.get_docker_name(),
                cmd=cmd_string,
            )
        )

        # Start the new docker container.
        result = self.host.cmd(cmd_string)

        print(
            "CMD executed by node: {name}\nResult: {result}"
            .format(
                name=self.get_docker_name(),
                result=result,
            )
        )
