#!/usr/bin/python2
import commands
import trparse
import requests
import csv
import sys
from distutils.spawn import find_executable

def traceroute(target):
    # I was gonna do this in Scapy but I value my Sanity.
    print "{+} Running traceroute on %s" %(target)
    trdata = commands.getoutput("traceroute %s" %(target))
    parse = trparse.loads(trdata)
    ipaddrs = []
    for hop in parse.hops:
        probe = hop.probes[0]
        ipaddrs.append(probe.ip)
    return ipaddrs

def main():
    print "{?} Checking $PATH for traceroute..."
    if find_executable("traceroute"):
        print "{+} Traceroute found in $PATH"
    else:
        sys.exit("{-} Traceroute not found")

    try:
        print "{+} Downloading our list of evil DDoS numbers..."
        r = requests.get("http://surveilling.me/stuff/evil_ips.csv")
    except Exception, e:
        sys.exit("Failed to download evil IP list. Abort!")
    # remember we have r.text object
    hosts = ['google.com', 'facebook.com', 'gmail.com', 'torproject.org', 'eff.org', 'hotmail.com', 'wikileaks.org'] # later have this as random ips
    hops = []
    print "{+} Beginning the traceroutes..."
    for host in hosts:
        ipaddrs = traceroute(target=host)
        for ipaddr in ipaddrs:
            hops.append(ipaddr)
    shitweasels = {}
    f = open("temp.txt", "wb") # tempfile gets nuked every time. this is a dirty hack because laziness.
    f.write(r.text)
    f.close()
    f = open('temp.txt')
    csv_r = csv.reader(f, delimiter=",")
    print "{+} And now for some data munging..."
    for row in csv_r:
        ipaddress = row[1]
        prodname = row[0]
        shitweasels[ipaddress] = prodname
    # now this is REALLY INEFFICIENT BUT I DONT FUCKING CARE
    for hop in hops:
        for ipaddress, prodname in shitweasels.iteritems():
            if hop == ipaddress:
                print "{+} SURVEILLANCE DETECTED! Product Name: %s  IP Address: %s" %(prodname, ipaddress)
    print "{+} Done! If surveillance shitweaselry was detected, take some precautions!!!"


if __name__ == "__main__":
    main()
