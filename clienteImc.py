import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
print ("*** MULTIPLICACIÓN***")
n1=float(input('Ingrese el primer número:'))
n2=float(input('Ingrese el segundo número:'))
print('el resultado es: ',getattr(proxy, 'multiply args')(n1, n2))
