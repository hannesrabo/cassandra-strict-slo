#!/bin/bash

# Setting the starting point.
REPO_PATH=$(git rev-parse --show-toplevel)
cd "$REPO_PATH/.."

# Cloning the cassandra fork
git clone https://github.com/hannesrabo/cassandra.git
cd cassandra
CLONED_PATH=$(pwd)

# Making data dirs
mkdir -p /slo/cassandra/data
mkdir -p /slo/cassandra/co
mkdir -p /slo/cassandra/saved_caches

# Copy configuration files
cp -R "$REPO_PATH/tools/res/*" "$CLONED_PATH/conf/"

