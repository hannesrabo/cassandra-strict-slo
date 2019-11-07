#!/usr/bin/env python
# Runs YCSB workload B on the Cassandra nodes.

import sys
import os

if len(sys.argv) <= 1:
	print "Please enter output file name and optionally ops/sec."
	exit()
if len(sys.argv) <= 2:
	print "No ops/sec given. YCSB will run max ops/sec."
else:
	op_sec = sys.argv[2]

rfile = sys.argv[1]

print ("Loading workloads...")
os.chdir("/home/csd/YCSB/")
os.system("./bin/ycsb load cassandra2-cql -p hosts='100.0.0.11,100.0.0.12,100.0.0.13,100.0.0.14' -P workloads/workloadb -s -threads 10 > slo_workload_load.out")
print "Loading... Done.."
print "Running workload..."

# If no ops/sec argument is given, YCSB runs at maximum ops/sec
if len(sys.argv) <= 2:
	os.system("./bin/ycsb run cassandra2-cql -p hosts='100.0.0.11,100.0.0.12,100.0.0.13,100.0.0.14' -P workloads/workloadb -s -threads 10" + " > " + rfile)

else:
	os.system("./bin/ycsb run cassandra2-cql -p hosts='100.0.0.11,100.0.0.12,100.0.0.13,100.0.0.14' -P workloads/workloadb -s -threads 10 -target " + op_sec + " > " + rfile)

print ("Benchmarking done...")
os.system("mv "+rfile+" /home/csd/cassandra-strict-slo/results")
print ("Results available in "+rfile+" in project root directory!")
