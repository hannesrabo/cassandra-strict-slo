#!/bin/bash

# Installing python
sudo apt install python3 python3-pip python3-venv

# Creating a virtual environment.
mkdir env-slo && python3 -m venv env-slo
source env-slo/bin/activate

# Setting up dependencies
pip3 install -r requirements.txt 

# Setting up githooks
REPO_PATH=$(git rev-parse --show-toplevel)
ln -s "$REPO_PATH/tools/pre-commit.sh" "$REPO_PATH/.git/hooks/pre-commit"