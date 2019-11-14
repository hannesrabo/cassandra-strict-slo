#!/usr/bin/env python
# Runs YCSB workload B on the Cassandra nodes.

import sys
import os

if len(sys.argv) <= 2:
    print("Please enter output file name, speculative retry threshold (ms) and optionally ops/sec.")
    exit()
if len(sys.argv) <= 3:
    print("No ops/sec given. YCSB will run max ops/sec.")
else:
    op_sec = sys.argv[3]

rfile = sys.argv[1]
threshold = sys.argv[2]

print("Loading workloads...")
os.chdir("/home/csd/YCSB/")
os.system("./bin/ycsb load cassandra2-cql -p hosts='100.0.0.11,100.0.0.12,100.0.0.13,100.0.0.14' -P workloads/workloadb -s -threads 10 &>/dev/null")
print("Loading... Done..")
print("Running workload...")

# Remove old performance files
os.system("rm -f /home/csd/cassandra-strict-slo/performance/*")

# If no ops/sec argument is given, YCSB runs at maximum ops/sec
target_string = ""
if len(sys.argv) > 3:
    target_string = " -target " + op_sec + " -p target=" + op_sec

os.system("./bin/ycsb run cassandra2-cql -p hosts='100.0.0.11,100.0.0.12,100.0.0.13,100.0.0.14' -p cassandra.speculative=" +
          threshold + " -P workloads/workloadb -s -threads 10" + target_string + " > " + rfile + " 2> " + rfile + "_stderr")

print("Benchmarking done...")

# Checking that the benchmark was finished
print("Checking benchmark")
file = open(rfile, "r")
benchmark_result = file.read()
if benchmark_result.find("[READ]") == -1:
    print("The benchmark is corrupt. Exiting")
    exit()


os.system("mv "+rfile+" /home/csd/cassandra-strict-slo/results")
os.system("mv "+rfile+"_stderr /home/csd/cassandra-strict-slo/results")

os.system("mkdir /home/csd/cassandra-strict-slo/results/"+rfile+"_metrics")
os.system("mv /home/csd/cassandra-strict-slo/performance/* /home/csd/cassandra-strict-slo/results/"+rfile+"_metrics")

print("Results available in "+rfile+" in results directory!")

