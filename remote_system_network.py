# Configure Remote System Network:
#Get System Stats(free memory,load average,routing table,uptime)

import paramiko
import time
from rich.console import Console

console = Console()

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print("connecting........")
ssh_client.connect(hostname="127.0.0.1",port=22,
			username="shanu",password="shanu") # client taking the remote pc

stdin,stdout,stderr = ssh_client.exec_command("free -m\n")
print(".................Free Memory....................")
mem = stdout.read().decode()
console.print(mem,style="bold blue")
time.sleep(2)

stdin,stdout,stderr = ssh_client.exec_command("uptime -s\n")
print("...............Uptime...........................")
up = stdout.read().decode()
console.print(up,style="bold blue")
time.sleep(2)

stdin,stdout,stderr = ssh_client.exec_command("cat /proc/loadavg\n")
print("......................Load Average...................")
load = stdout.read().decode()
console.print(load,style="bold blue")
time.sleep(2)

stdin,stdout,stderr = ssh_client.exec_command("route -n\n")
print("......................Routing table..............")
route = stdout.read().decode()
console.print(route,style="bold blue")

if ssh_client.get_transport().is_active() == True:
	print("Disconnecting.........")
	ssh_client.close()

