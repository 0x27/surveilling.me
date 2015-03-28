#!/usr/bin/python2
"""
Shodanized Mass Scan Shit. I gotta refactor this shit later 
"""
import shodan

def loggit(ip, shitweasel):
    logfile = "/var/www/stuff/evil_ips.csv"
    f = open(logfile, "a+")
    f.write(shitweasel+","+ip+"\n")
    f.close()

SHODAN_API_KEY = "qSWcO6uyP6g3Sk3gTc9jbos1QZA5b6Yu" #random key
api = shodan.Shodan(SHODAN_API_KEY)
# Wrap the request in a try/ except block to catch errors

def scan_cisco_li():
    try:
        # Search Shodan
        results = api.search('ADVENTERPRISEK9_IVS_LI-M')
        # Show the results
        print '{+} CISCOS WITH LI MODE ENABLED FOUND: %s' % results['total']
        for result in results['matches']:
            print '{!} INTERCEPTOR DISCOVERED: %s' % result['ip_str']
            loggit(ip=result['ip_str'], shitweasel="Cisco with Lawful Intercept Enabled")
    except shodan.APIError, e:
        print 'Error: %s' % e

def scan_bluecoat_proxysg():
    try:
        # Search Shodan
        results = api.search('ProxySG')
        # Show the results
        print '{+} BLUECOAT SHITLORDS FOUND: %s' % results['total']
        for result in results['matches']:
            print '{!} INTERCEPTOR DISCOVERED: %s' % result['ip_str']
            loggit(ip=result['ip_str'], shitweasel="Bluecoat Shitweasels")
    except shodan.APIError, e:
        print 'Error: %s' % e
        
def scan_bluecoat_misc():
    try:
        # Search Shodan
        results = api.search('Blue Coat')
        # Show the results
        print '{+} More BLUECOAT SHITLORDS FOUND: %s' % results['total']
        for result in results['matches']:
            print '{!} INTERCEPTOR DISCOVERED: %s' % result['ip_str']
            loggit(ip=result['ip_str'], shitweasel="Bluecoat Shitweasels")
    except shodan.APIError, e:
        print 'Error: %s' % e
        
def scan_packeteer(): # Packeteer
    try:
        # Search Shodan
        results = api.search('Packeteer')
        # Show the results
        print '{+} PACKETEERS FOUND: %s' % results['total']
        for result in results['matches']:
            print '{!} INTERCEPTOR DISCOVERED: %s' %(result['ip_str'])
            loggit(ip=result['ip_str'], shitweasel="Packeteer Shitweasels")
    except shodan.APIError, e:
        print 'Error: %s' %(e)
        
scan_cisco_li()
scan_bluecoat_proxysg()
scan_bluecoat_misc()
scan_packeteer()
