sudo mn -c

sudo kill $(ps aux | grep cassandra | grep root | awk '{print $2}')

