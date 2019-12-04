#!/usr/bin/env python
# Runs all workloads with different ops/sec.

import sys
import os
import numpy as np


if len(sys.argv) != (1 + 7):
    print("Expected 7 arguments")
    print("Usage: run_some_benchmark.py <filename-prefix> <first-target> <last-target> <step-target> <first-threshold> <last-threshold> <step-threshold>")
    print("")
    print("filename-prefix: The prefix for the different filenames")
    print("")
    print("first-target:    The lowest ops/sec target")
    print("last-target:     The highest ops/sec target")
    print("step-target:     How much between the ops/sec targets")
    print("")
    print("first-threshold: The lowest speculative retry threshold")
    print("last-threshold:  The highest speculative retry threshold")
    print("step-threshold:  How much between the speculative retry thresholds")
    print("")
    print("Example:")
    print("run_some_benchmark.py bench_result 200 800 300 3 5 2")
    print("This will run benchmarks with the following parameters:")
    print("200 ops/sec, 3ms threshold")
    print("500 ops/sec, 3ms threshold")
    print("800 ops/sec, 3ms threshold")
    print("200 ops/sec, 5ms threshold")
    print("500 ops/sec, 5ms threshold")
    print("800 ops/sec, 5ms threshold")
    exit()

filename_prefix = sys.argv[1]
first_target = int(sys.argv[2])
last_target = int(sys.argv[3])
step_target = int(sys.argv[4])
first_threshold = int(sys.argv[5])
last_threshold = int(sys.argv[6])
step_threshold = int(sys.argv[7])


operation_targets = range(first_target, last_target + 1, step_target)
sr_thresholds = range(first_threshold, last_threshold + 1, step_threshold)

for threshold in sr_thresholds:
    for target in operation_targets:
        filename = filename_prefix + "_" + str(threshold) + "_" + str(target)
        print("Running benchmark for file: " + filename)
        os.system("./tools/run_workload.py " + filename +
                  " " + str(threshold) + " " + str(target))
