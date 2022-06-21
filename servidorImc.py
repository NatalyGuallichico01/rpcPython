from ast import Div
from xmlrpc.server import SimpleXMLRPCServer

from cv2 import divide

server = SimpleXMLRPCServer(('localhost', 9000))

#def imc(*args):
def my_function(n1, n2):
    total=n1*n2
    #return (peso/(altura*altura))
    return total


server.register_function(my_function, 'multiply args')

try:
    print('Press Ctrl + c to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Thank you')