#!/usr/bin/env python
# Runs 2 YCSB clients with workload B on the Cassandra nodes.

import subprocess
import psutil
import time
import os
import sys
import shlex
from datetime import datetime

if len(sys.argv) < 3:
    print("Expected 2 arguments")
    print("Usage: liquorice.py <filename-prefix> <sr-throshold>")
    print("")
    print("filename-prefix: The prefix for the different filenames")
    print("sr-threshold:    The level of sr-threshold in ms. If set to 0 it runs a dynamicly chosen speculative retry.")
    exit()

rfile = sys.argv[1]
threshold = sys.argv[2]

print("\nLoading workloads...")
os.chdir("/home/csd/YCSB/")
client1_out = open(rfile+"_Client1",'w')
client2_out = open(rfile+"_Client2",'w')
client1_out.write(str(datetime.now()))
#client2_out.write(str(datetime.now()))
#os.system("echo '' > "+rfile+"_stderr_Client1")
ycsb1_cmd_load = "python bin/ycsb load cassandra2-cql -p hosts='100.0.0.11,100.0.0.12,100.0.0.13,100.0.0.14' -P workloads/workloadb -threads 12 -s" #> slo_workload_load_client1.out"
ycsb2_cmd_load = "python bin/ycsb load cassandra2-cql -p hosts='100.0.0.11,100.0.0.12,100.0.0.13,100.0.0.14' -P workloads/workloadb_short -threads 12 -s"
ycsb1_load = subprocess.Popen(shlex.split(ycsb1_cmd_load),stdout=client1_out,stderr=client1_out)# -s > slo_workload_load_client1.out").split(),stdout=subprocess.PIPE)
ycsb2_load = subprocess.Popen(shlex.split(ycsb2_cmd_load),stdout=client2_out,stderr=client2_out)
while ycsb1_load.poll()==None:
    print("Loading YCSB1")
    time.sleep(10)
client1_out.close()
#while ycsb2_load.poll()==None:
#    print("Loading YCSB2")
#    time.sleep(10)
client2_out.close()
ycsb2_cmd_run = "python bin/ycsb run cassandra2-cql -p hosts='100.0.0.11,100.0.0.12,100.0.0.13,100.0.0.14' -P workloads/workloadb_short -threads 12 -target 2000 -s -p cassandra.speculative=" + threshold + " -p performance.prefix=Client1"
ycsb1_cmd_run = "python bin/ycsb run cassandra2-cql -p hosts='100.0.0.11,100.0.0.12,100.0.0.13,100.0.0.14' -P workloads/workloadb -threads 12 -s -p cassandra.speculative=" + threshold + " -p performance.prefix=Client2"
print("\nRunning workloads")
client1_out = open(rfile+"_Client1",'a')
client2_out = open(rfile+"_Client2",'a')
ycsb1 = subprocess.Popen(shlex.split(ycsb1_cmd_run),stdout=client1_out,stderr=client1_out) #Runs for 8 mins
#ycsb2 = subprocess.Popen(shlex.split(ycsb2_cmd_run),stdout=client2_out,stderr=client2_out) # Runs for 40 sec
print('Client1 is running')
#time.sleep(30)
while ycsb1.poll()==None:
    ycsb2 = subprocess.Popen(shlex.split(ycsb2_cmd_run),stdout=client2_out,stderr=client2_out) # Runs for 40 sec
    #p = psutil.Process(ycsb2.pid)
    #p.suspend()
    #print("Paused client2 "+str(datetime.now()))
    #time.sleep(60)
    while ycsb2.poll()==None:
        print("Client2 is running")
        time.sleep(10)
    print("Client2 Finished rerunning in 50 seconds")
    time.sleep(50)
    if ycsb1.poll()!=None:
       break
    #time.sleep(60)
#time.sleep(6000)
print('YCSB1 and YCSB2 has finished Running')
#while ycsb2.poll()==None:
#    i = 0
#    time.sleep(10)
#    if ycsb2.poll()!=None:
#        break
os.system("mv "+rfile+"_Client1"+" /home/csd/cassandra-strict-slo/results")
os.system("mv "+rfile+"_Client2"+" /home/csd/cassandra-strict-slo/results")  
#os.system("mv "+rfile+"_stderr_Client1 /home/csd/cassandra-strict-slo/results")
#os.system("mv "+rfile+"_stderr_Client2 /home/csd/cassandra-strict-slo/results")
os.system("sudo mkdir /home/csd/cassandra-strict-slo/results/"+rfile+"_metrics")
os.system("sudo mv /home/csd/cassandra-strict-slo/performance/* /home/csd/cassandra-strict-slo/results/"+rfile+"_metrics")
