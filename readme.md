tfernandez/docker_knocker
=========================
An ultra-small python based port knocker to periodically knock on the ports of a remote server.

I built this because I got lazy to knock on the ports at my parents house to open them. I wanted my docker server at my house to maintain a port knock connection.

How To Use
----------
The docker container requires a few variables to work. 
| ENV Variable | Description |
|--------------|-------------|
|**IP**        |Enter here the IP or Hostname of the destination. `Default: 1.1.1.1`|
|**PORTS**     |Ports and Protocol combinations. `Default: 1234:tcp,4321:udp`|
|**INTERVAL_IN_MIN**|The knock interval. In other words, how frequently the container will knock at the destination. `Default: 60`|
|**DELAY_IN_SEC**|The delay between knocks `Default: 5`|

Sample Docker Command
-
docker run -e IP=domain&#46;com -e PORTS='1111:tcp,2222:udp' -e DELAY_IN_SEC=5 -e INTERVAL_IN_MIN=60 pyknocker