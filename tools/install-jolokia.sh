# Getting the stats collection plugin from github
mkdir /opt/jolokia
cd /opt/jolokia
wget https://github.com/rhuss/jolokia/releases/download/v1.4.0/jolokia-1.4.0-bin.tar.gz
tar -xf jolokia-1.4.0-bin.tar.gz

# Adding the option to the config file
REPO_PATH=$(git rev-parse --show-toplevel)
cd "$REPO_PATH/.."
echo 'JVM_OPTS="$JVM_OPTS -javaagent:/opt/jolokia/jolokia-1.4.0/agents/jolokia-jvm.jar"' >> "$CLONED_PATH/conf/cassandra/cassandra-env.sh"
