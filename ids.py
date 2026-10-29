from scapy.all import sniff, IP, TCP

ports = {}

def detect(p):
    if IP in p and TCP in p:
        ip = p[IP].src
        port = p[TCP].dport

        ports.setdefault(ip, set()).add(port)

        if len(ports[ip]) == 5:
            print("ALERT! Possible port scan from", ip)

print("IDS started...")
sniff(filter="tcp", prn=detect, store=False)

sudo python3 ids.py
sudo python3 -c "from scapy.all import *; [send(IP(dst='127.0.0.1')/TCP(dport=p,flags='S'),verbose=False) for p in range(8001,8006)]"
