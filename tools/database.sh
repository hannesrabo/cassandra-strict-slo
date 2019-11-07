#!/bin/bash

#Check if cassandra is up
while true; do if (netstat -plnt | grep 9042 > /dev/null 2>&1); then break; sleep 2;fi done
echo "Cassandra is up...."


#Get IP address of the node
IP_ADDRESS=$(ip address | grep inet | grep 24 | awk '{print $2}' | cut -f1 -d/) 


cqls() {
 ../cassandra/bin/cqlsh $IP_ADDRESS -e "$1"
}

#CQLS commands
cqls "show host"
cqls "describe ycsb;" || cqls "create keyspace ycsb WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor': 2 };"
cqls "describe ycsb.usertable" || cqls "USE ycsb;create table IF NOT EXISTS usertable ( y_id varchar primary key, field0 varchar, field1 varchar, field2 varchar, field3 varchar, field4 varchar, field5 varchar, field6 varchar, field7 varchar, field8 varchar, field9 varchar);"


echo "Database is up.. "
echo "Preparing for benchmarking..."
