import sys, time, socket
from splunklib.searchcommands import \
    dispatch, GeneratingCommand, Configuration, Option, validators

@Configuration()
class UDPCommand(GeneratingCommand):
    #count = Option(require=True, validate=validators.Integer())
    port = Option(require=True, validate=validators.Integer())
    message = Option(require=True)
    ip = Option(require=True)

    def generate(self):
	IPADDR = self.ip
	PORTNUM = self.port
	PACKETDATA = self.message

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
	s.settimeout(5)
	try:
    # connect the socket, think of it as connecting the cable to the address location
		s.connect((IPADDR, PORTNUM))
 
    # send the command
		s.send(PACKETDATA)
	except:
    		pass
 
	data = s.recv(4096).decode("UTF-8")
#for i in range(1, self.count + 1):
	#yield {'_time': time.time(), 'event_no': i, '_raw': data }
	yield {'_time': time.time(), '_raw': data }

# Recieve UDP response
#data = s.recv(4096)

# close the socket
	s.close()

dispatch(UDPCommand, sys.argv, sys.stdin, sys.stdout, __name__)
