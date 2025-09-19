from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>sample page</title>
    </head>
    <body>
        <h1 align="center">DEVICE SPECIFICATION-25015718</h1>
        <table border="3" cellpadding="25">
            <tr>
                <th>S.NO</th>
                <th>Specification</th>
                <th>Description</th>
            </tr>
            <tr>
                <td>1.</td>
                <td>Storage</td>
                <td>954 GB</td>
            </tr>
            <tr>
                <td>2.</td>
                <td>Graphics Card</td>
                <td>128 MB</td>
            </tr>
            <tr>
                <td>3.</td>
                <td>Installed RAM</td>
                <td>16.0 GB</td>
            </tr>
            <tr>
                <td>4.</td>
                <td>Processor</td>
                <td>Intel(R) core(TM) Ultra 5 125H</td>
            </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()