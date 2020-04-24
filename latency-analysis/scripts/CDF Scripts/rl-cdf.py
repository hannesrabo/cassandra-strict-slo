import os

import pandas as pd

import glob

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

import numpy as np




all_folders = glob.glob("/home/csd/cassandra-strict-slo/results/phase3_final_*_metrics/")


for i in range(len(all_folders)):
        all_files = glob.glob(all_folders[i]+"state*")

        subfile     = all_files[0]

        folder2scan = subfile[:subfile.rfind("/")]

        print("> scanning " + folder2scan)

        li = []

        for filename in all_files:

                        df = pd.read_csv(filename)

			li.append(df)


        frame = pd.concat(li, ignore_index=True)

        frame2 = frame[[" ReadLatency1", " WriteLatency1"]]


        mu = frame2[' ReadLatency1'].mean()

        sigma = frame2[' ReadLatency1'].std()


        fig, ax = plt.subplots(figsize=(8, 4))  #fig is the figure and ax is a axes.Axes object. 

        # plot the cumulative histogram

        n_bins = np.arange(max(frame2[' ReadLatency1']) +1)

        n, bins, patches = ax.hist(frame2[' ReadLatency1'], n_bins, density=True, histtype='step', cumulative=True, label='Empirical')




        # Add a line showing the expected distribution.

        y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))

        y = y.cumsum()

        y /= y[-1]

        ax.plot(bins, y, 'k--', label='Theoretical')




        ax.grid(True)

        ax.legend(loc='best')

        ax.set_title('CDF')

        ax.set_xlabel('Read Latency (microseconds)')

        ax.set_ylabel('Likelihood of occurrence')

        ax.set_yticks(np.arange(0,1.01,step=0.1))

	plt.savefig("{}_ReadLatency-CDF.png".format(i))



        plt.close(fig)



