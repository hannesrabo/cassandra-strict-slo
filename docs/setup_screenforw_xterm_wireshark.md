# Setup screen forwarding for GUI programs running on the server

  - [Configure SSH for -X forwarding](#configure-ssh-for--x-forwarding)
  - [Run Wireshark](#run-wireshark)
  - [Run Xterm](#run-xterm)

## Configure SSH for -X forwarding

### On the server

#### Go to the ssh config file
`cd /etc/ssh/ssh_config`

####  Locate the line that says “ForwardX11”
Uncomment and change "no" to "yes."

#### Reboot the SSH server
`systemctl restart sshd.service`

### On the client
**If on Linux:**

`ssh user@ip -X`

**If on Mac:**

Install XQuartz, open the XQuartz shell and ssh from there.

**If on Windows:**

Install Xming, open the Xming shell and ssh from there.

## Run Wireshark
Having initiated a ssh -X session to the server, open the Mininet shell, then run

`h1 wireshark
`

## Run Xterm

Having initiated a ssh -X session to the server, open the Mininet shell, then run

`xterm h1
`
