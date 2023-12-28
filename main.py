import subprocess


file_path = 'ip.txt'  
with open(file_path, 'r') as file:
    ip_ranges = file.readlines()
    ip_ranges = [ip.strip() for ip in ip_ranges if ip.strip()]
for range in ip_ranges:
    subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", range, "-j", "DROP"])
