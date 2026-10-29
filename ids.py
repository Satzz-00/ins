
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
