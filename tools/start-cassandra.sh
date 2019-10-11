#!/bin/bash

REPO_PATH=$(git rev-parse --show-toplevel)

CASSANDRA_HOME="$REPO_PATH/../cassandra"
CASSANDRA_CONF="$CASSANDRA_HOME/conf"
PATH=$PATH:"$CASSANDRA_HOME/bin"

JAVA_HOME="/usr/lib/jvm/default-java"

source "$CASSANDRA_HOME/bin/cassandra.in.sh"

IP_ADDRESS=$(ip address | grep inet | grep 24 | awk '{print $2}' | cut -f1 -d/)

CASSANDRA_CLUSTER_NAME="CassandraMininetCluster"
CASSANDRA_BROADCAST_ADDRESS="$IP_ADDRESS"

CASSANDRA_SEEDS="100.0.0.11"

CASSANDRA_BROADCAST_RPC_ADDRESS="$IP_ADDRESS"
CASSANDRA_LISTEN_ADDRESS="$IP_ADDRESS"
CASSANDRA_RPC_ADDRESS="$IP_ADDRESS"

echo "This node is running with IP $IP_ADDRESS"

echo "Running"

cp "$REPO_PATH/tools/res/cassandra.yaml" /slo/cassandra/cassandra.yaml

source "$REPO_PATH/tools/res/create-config.sh"

. "$REPO_PATH/../cassandra/bin/cassandra" -R -d

echo "Started cassandra node at: $IP_ADDRESS"

