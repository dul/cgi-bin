import json

print 'Content-Type: text/html'
print

f = open("cgi-bin/poligonos.txt")


print str(json.loads(f.readlines()[0]))
