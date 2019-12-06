#!/bin/bash

# Setting the starting point.
REPO_PATH=$(git rev-parse --show-toplevel)
cd "$REPO_PATH/.."

# Cloning the cassandra fork
git clone https://github.com/hannesrabo/cassandra.git
cd cassandra
CLONED_PATH=$(pwd)

# Making data dirs
mkdir -p /slo/cassandra
chown -R csd:csd /slo/cassandra

# Copy configuration files
cp "$REPO_PATH/tools/res/cassandra.yaml" "$CLONED_PATH/conf/cassandra.yaml"
cp "$REPO_PATH/tools/res/cassandra-env.sh" "$CLONED_PATH/conf/cassandra-env.sh"

mv "$CLONED_PATH/conf/cassandra.yaml" /slo/cassandra/cassandra.yaml
ln -s /slo/cassandra/cassandra.yaml "$CLONED_PATH/conf/cassandra.yaml"

apt install ant
CASSANDRA_USE_JDK11=true ant

