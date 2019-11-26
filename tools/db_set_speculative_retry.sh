#!/bin/bash

#Get IP address of the node
IP_ADDRESS=$(ip address | grep inet | grep 24 | awk '{print $2; exit}' | cut -f1 -d/) 
TARGET_SPECULATIVE_RETRY=$1

cqls() {
    echo "EXECUTING: . /home/csd/cassandra/bin/cqlsh $IP_ADDRESS -e $1"
    . /home/csd/cassandra/bin/cqlsh $IP_ADDRESS -e "$1"
}

cqls "ALTER TABLE ycsb.usertable WITH speculative_retry = '$TARGET_SPECULATIVE_RETRY';"
