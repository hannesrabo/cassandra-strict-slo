#!/bin/bash

# This files run everytime a commit is done. It can be used to
# change the code.

REPO_PATH=$(git rev-parse --show-toplevel)

$REPO_PATH/tools/scripts/ptformat