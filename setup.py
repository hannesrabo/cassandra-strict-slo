from setuptools import setup

setup(
    name='cassandra-slo',
    version='1.0',
    description='Module for setting up virtual network of Cassandra hosts',
    author='Hannes Rabo, Julius Celik, Pethrus Gärdbom, Kamil Nasr, Shubhanker Singh, Vinayak Tejankar',
    author_email='hrabo@kth.se, jcelik@kth.se, gardborn@kth.se, knasr@kth.se, shusin@kth.se, tejankar@kth.se',
    packages=['cassandra-slo'],
    scripts=['tools/bin/pttestscript']
)
