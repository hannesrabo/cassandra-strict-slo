import os

import pandas as pd

import glob

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

import numpy as np




all_folders = glob.glob("/home/csd/cassandra-strict-slo/results/phase3_final_*_metrics/")
all_folders_box = {}


for i in range(len(all_folders)):
        if (all_folders[i].split('_')[2]!="hightarget"):
                if int(all_folders[i].split('_')[4]) in all_folders_box:
                        all_folders_box[int(all_folders[i].split('_')[4])].append(all_folders[i])
                else:
                        all_folders_box[int(all_folders[i].split('_')[4])]=[]
                        all_folders_box[int(all_folders[i].split('_')[4])].append(all_folders[i])


plt.figure(1)

frames_read = []
frames_write=[]

folders_box_keys = list(all_folders_box.keys())
for i in range(len(all_folders_box)):

    print("\n")
    print("==================== Throughput: "+str(folders_box_keys[i])+" ================================")
    print("\n")

    all_files=[]
    for j in range(len(all_folders_box[folders_box_keys[i]])):
        all_files = all_files + glob.glob(all_folders_box[folders_box_keys[i]][j]+"state*")

    li = []

    for filename in all_files:
        print("reading " + filename)
        df = pd.read_csv(filename)

        li.append(df)

    frame = pd.concat(li, ignore_index=True)



    frame2 = frame[[" ReadLatency1", " WriteLatency1"]]

    frames_read.append(frame2[' ReadLatency1'])
    frames_write.append(frame2[' WriteLatency1'])



## sorts the boxplots
sorted_frames       = [x for _,x in sorted(zip(folders_box_keys, frames_read))]
sorted_frames_write = [x for _,x in sorted(zip(folders_box_keys, frames_write))]
sorted_throughput   = [x for x,_ in sorted(zip(folders_box_keys, frames_read))]


plt.boxplot(sorted_frames, showfliers=False)
plt.xticks(xrange(1, len(all_folders_box.keys()) +1, 1), sorted_throughput) #xticks(ticks, [labels])
plt.xlabel("Throughput")
plt.ylabel("Read Latency")
plt.title("Latency per Throughput")
plt.savefig("Boxplot-rl-thr.png", bbox_inches='tight')

plt.figure(2)
plt.boxplot(sorted_frames_write, showfliers=False)
plt.xticks(xrange(1, len(all_folders_box.keys()) +1, 1), sorted_throughput)
plt.xlabel("Throughput")
plt.ylabel("Write Latency")
plt.title("Latency per Throughput")
plt.savefig("Boxplot-wl-thr.png", bbox_inches='tight')


