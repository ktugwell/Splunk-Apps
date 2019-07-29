import sys, time, socket, requests
from splunklib.searchcommands import \
    dispatch, GeneratingCommand, Configuration, Option, validators

@Configuration()
class SplunkRestCommand(GeneratingCommand):
    host = Option(require=True)
    token = Option(require=True)
    endpoint = Option(require=True)
    method = Option(require=False)
    output = Option(require=False)

    def generate(self):
	HOST = self.host
	TOKEN = self.token
	ENDPOINT = self.endpoint
        METHOD = self.method or "GET"
        OUTPUT = self.output or "json"

	try:
            headers = {
                 'Authorization': "Bearer " + TOKEN,
    'Cache-Control': "no-cache"
    }

	except:
    		pass
     
        response = requests.request(METHOD, HOST + ENDPOINT + "?output_mode=" + OUTPUT, headers=headers, verify=False)
	yield {'_time': time.time(), '_raw': response.text }



dispatch(SplunkRestCommand, sys.argv, sys.stdin, sys.stdout, __name__)
