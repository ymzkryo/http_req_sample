from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import json


class Http_Req_Sample(SimpleHTTPRequestHandler):

    def do_GET(self):

        uri = self.path
        ret = parse_qs(urlparse(uri).query, keep_blank_values = True)

        if ('foo' in ret.keys()) and (ret['foo'][0] == 'bar'):
            ret = json.dumps({ 'msg': 'ok' })
        else:
            ret = json.dumps({ 'msg': 'failure' })

        body = bytes(ret, 'utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-length', len(body))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        try:
            content_len=int(self.headers.get('content-length'))
            requestBody = json.loads(self.rfile.read(content_len).decode('utf-8'))

            response = { 'status' : 200,
                         'result' : {'hoge' : 100 ,'bar' : 'bar'}
                         }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            responseBody = json.dumps(response)

            self.wfile.write(responseBody.encode('utf-8'))
        except Exception as e:
            print("An error occured")
            print("The information of error is as following")
            print(type(e))
            print(e.args)
            print(e)
            response = { 'status' : 500,
                         'msg' : 'An error occured' }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            responseBody = json.dumps(response)

            self.wfile.write(responseBody.encode('utf-8'))


host = 'localhost'
port = 8000
httpd = HTTPServer((host, port), Http_Req_Sample)
print('serving at port', port)
httpd.serve_forever()
