# surveilling.me
Surveilling.me - Tests routes you are using for surveillance equipment

## Howto:
Download the client in client/client.py  
Install the required dependencies using "pip".  
These are: requests, and trparse.  
```
pip install requests trparse
```
Use a linux box with "traceroute" installed on it.  
Run client.py, no arguments. Just run it.

## How does it work.
It does a traceroute to a few sites (later to be random IP addresses), parses out the traceroute data of hops, downloads a list of bad IP's that are known-spy-boxes, and checks if any 
of your hops are on the list of bad shit. If they are, take some evasive action. If they aren't, well, you are probably fucked anyway as we only have limited internet visibility.

## Server Side Shit
I have a script using the Shodan API and some random API key I have been using for the past age that searches for known-bad stuff and gets IP lists to add to the canonical list of 
evil. This script is ran by cron every few hours and updates/replaces the bad IP's csv file.

## Web Stuff
Really crap onepage site done using a bootstrap generator out of laziness because I had spent fucking all day working on a JSON API, got bored, realized there was a lazy solution, and 
went with the lazy solution.

## Todo
Make it all less shit, implement our own scans, random IP generation, get a SSL cert, and generally make this actually useable for the end user and not just an academic curiosity.

