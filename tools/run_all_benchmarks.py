#!/usr/bin/env python
# Runs all workloads with different ops/sec.

import sys
import os
import numpy as np


if len(sys.argv) <= 1:
    print("Please enter a filename prefix")
    exit()

filename_prefix = sys.argv[1]
operation_targets = np.arange(400, 3600, 200).tolist()
sr_thresholds = np.arange(1, 20, 1).tolist()

for threshold in sr_thresholds:
    for target in operation_targets:
        filename = filename_prefix + "_" + str(threshold) + "_" + str(target)
        print("Running benchmark for file: " + filename)
        os.system("./tools/run_workload.py " + filename +
                  " " + str(threshold) + " " + str(target))
