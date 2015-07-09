#!/usr/bin/python2
"""
Shodanized Mass Scan Shit. I gotta refactor this shit later 
"""
import shodan

def loggit(ip, shitweasel): # I should make a better CSV output or perhaps JSON instead...
    logfile = "/var/www/stuff/evil_ips.csv"
    f = open(logfile, "a+")
    f.write(shitweasel+","+ip+"\n")
    f.close()

def scan_cisco_li(api):
    try:
        # Search Shodan - I need more model numbers to search for
        results = api.search('ADVENTERPRISEK9_IVS_LI-M')
        # Show the results
        print '{+} CISCOS WITH LI MODE ENABLED FOUND: %s' % results['total']
        for result in results['matches']:
            print '{!} INTERCEPTOR DISCOVERED: %s' % result['ip_str']
            loggit(ip=result['ip_str'], shitweasel="Cisco with Lawful Intercept Enabled")
    except shodan.APIError, e:
        print 'Error: %s' % e

def scan_bluecoat_proxysg(api):
    try:
        # Search Shodan - this query is fairly alright
        results = api.search('ProxySG')
        # Show the results
        print '{+} BLUECOAT SHITLORDS FOUND: %s' % results['total']
        for result in results['matches']:
            print '{!} INTERCEPTOR DISCOVERED: %s' % result['ip_str']
            loggit(ip=result['ip_str'], shitweasel="Bluecoat Shitweasels")
    except shodan.APIError, e:
        print 'Error: %s' % e
        
def scan_bluecoat_misc(api):
    try:
        # Search Shodan - this query may have FP's
        results = api.search('Blue Coat')
        # Show the results
        print '{+} More BLUECOAT SHITLORDS FOUND: %s' % results['total']
        for result in results['matches']:
            print '{!} INTERCEPTOR DISCOVERED: %s' % result['ip_str']
            loggit(ip=result['ip_str'], shitweasel="Bluecoat Shitweasels")
    except shodan.APIError, e:
        print 'Error: %s' % e
        
def scan_packeteer(api): # Packeteer
    try:
        # Search Shodan - this one found some interesting stuff
        results = api.search('Packeteer')
        # Show the results
        print '{+} PACKETEERS FOUND: %s' % results['total']
        for result in results['matches']:
            print '{!} INTERCEPTOR DISCOVERED: %s' %(result['ip_str'])
            loggit(ip=result['ip_str'], shitweasel="Packeteer Shitweasels")
    except shodan.APIError, e:
        print 'Error: %s' %(e)

def main():
    SHODAN_API_KEY = "qSWcO6uyP6g3Sk3gTc9jbos1QZA5b6Yu" #random key from someones github repo. I was going to make it handle a list of keys but forgot. so thats a TODO...
    api = shodan.Shodan(SHODAN_API_KEY)
    scan_cisco_li(api=api)
    scan_bluecoat_proxysg(api=api)
    scan_bluecoat_misc(api=api)
    scan_packeteer(api=api)

if __name__ == "__main__":
    main()
