# Steps to set up the Mininet topology
## Prerequisites
Mininet is already installed.

## Steps
### Step 1 - Add the topology file
File name: topology_slo.py

### Step 2 - Install the ovs-testcontroller

`sudo apt-get install openvswitch-testcontroller`

### Step 3 - Alias the controller

Alias openvswitch-controller with ovs-controller.


`sudo cp /usr/bin/ovs-testcontroller /usr/bin/ovs-controller`
### Step 4 - Find the PID of the openvswitch-testcontroller
`ps -ef | grep ovs-testcontroller
`
### Step 5 - Stop the openvswitch-testcontroller
`kill <PID of ovs-testcontroller>
`
### Step 6 - Run the topology
`sudo python topology_slo.py
`
### Step 7 - See if the topology is working
In the Mininet shell, run:


`pingall
`

## Afterthoughts
Even though the switch used is a simple L2 switch and no L3 routing (e.g. IP) is required, Mininet still requires a controller. According to the [documentation](http://www.openvswitch.org//support/dist-docs/ovs-testcontroller.8.html "document") of the ovs-testcontroller:

> it is  a  simple  OpenFlow controller that manages any number of switches over the OpenFlow protocol, causing them to function as  L2 MAC-learning switches or hubs.


# Things to consider when running Mininet

### Close Mininet in the shell interface
` exit`

### IMPORTANT: Always run clean as well after closing Mininet
`mn -c`
