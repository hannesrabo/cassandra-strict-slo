# Running the Mininet topology
## Prerequisites
Mininet is already installed.

## Steps to Setup
### Step 1 - Add the topology file
File name: topology_slo.py

### Step 2 - Install the ovs-testcontroller

```sh
sudo apt-get install openvswitch-testcontroller
```

### Step 3 - Alias the controller

Alias openvswitch-controller with ovs-controller.


```sh
sudo cp /usr/bin/ovs-testcontroller /usr/bin/ovs-controller
```

### Step 4 - Find the PID of the openvswitch-testcontroller
```sh
ps -ef | grep ovs-testcontroller
```
### Step 5 - Stop the openvswitch-testcontroller
```sh
kill <PID of ovs-testcontroller>
```

### Step 6 - Run the topology
```sh
sudo python topology_slo.py
```

### Step 7 - See if the topology is working
In the Mininet shell, run:


```sh
pingall
```

## Afterthoughts
Even though the switch used is a simple L2 switch and no L3 routing (e.g. IP) is required, Mininet still requires a controller. According to the [documentation](http://www.openvswitch.org//support/dist-docs/ovs-testcontroller.8.html "document") of the ovs-testcontroller:

> it is  a  simple  OpenFlow controller that manages any number of switches over the OpenFlow protocol, causing them to function as  L2 MAC-learning switches or hubs.


## Things to consider when running Mininet

### Close Mininet in the shell interface
```sh
exit
```

### IMPORTANT: Always run clean as well after closing Mininet
```sh
mn -c
```
