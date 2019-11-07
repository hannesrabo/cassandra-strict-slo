#!/usr/bin/env python
# Runs all workloads with different ops/sec.

import sys
import os

if len(sys.argv) <= 1:
    print ("Please enter a filename prefix")
    exit()

filename_prefix = sys.argv[1]
operation_targets = [500, 600, 700, 800, 900, 1000, 1100, 1200]

for target in operation_targets:
    filename = filename_prefix + "_" + str(target)
    print ("Running benchmark for file: " + filename)
    os.system("./tools/run_workload.py " + filename + " " + str(target))

