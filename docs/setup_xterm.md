# Setup screen forwarding for GUI programs running on the server

## Configure SSH for -X forwarding

### On the server

#### Go to the ssh config file
`cd /etc/ssh/ssh_config`

####  Locate the line that says “ForwardX11”
Uncomment and change "no" to "yes."

#### Reboot the SSH server
`systemctl restart sshd.service`

### On the client
ssh user@ip -X
