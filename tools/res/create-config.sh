#!/bin/bash

CASSANDRA_CONFIG=$CASSANDRA_CONF
CASSANDRA_DATA="/slo/cassandra"
echo "Creating config : $CASSANDRA_CONF"

_sed-in-place() {

	local filename="$1"; shift

	local tempFile

	tempFile="$(mktemp)"

	sed "$@" "$filename" > "$tempFile"

	cat "$tempFile" > "$filename"

	rm "$tempFile"

}

_sed-in-place "$CASSANDRA_DATA/cassandra.yaml" \
	-r 's/(- seeds:).*/\1 "'"$CASSANDRA_SEEDS"'"/'

for yaml in \
	broadcast_address \
	broadcast_rpc_address \
	cluster_name \
	endpoint_snitch \
	listen_address \
	num_tokens \
	rpc_address \
	start_rpc \
; do
	var="CASSANDRA_${yaml^^}"
	val="${!var}"

	echo "Setting $var=$val"
	if [ "$val" ]; then
		_sed-in-place "$CASSANDRA_DATA/cassandra.yaml" \
			-r 's/^(# )?('"$yaml"':).*/\2 '"$val"'/'
	fi
done


for rackdc in dc rack; do
	var="CASSANDRA_${rackdc^^}"
	val="${!var}"

	if [ "$val" ]; then
		_sed-in-place "$CASSANDRA_CONFIG/cassandra-rackdc.properties" \
			-r 's/^('"$rackdc"'=).*/\1 '"$val"'/'
	fi
done
