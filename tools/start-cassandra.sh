#!/bin/bash

REPO_PATH=$(git rev-parse --show-toplevel)

./"$REPO_PATH/../cassandra/bin/cassandra" -f
