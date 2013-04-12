import jsonToKml
import logFunctions
import sys
import random
import os
import string
import urllib



#~ 
#~ 
''' Lista de colores para las capas '''
colores = ['7f3300ff','7f33ff00','7f33ffff', '7f990000', '7f99cc33', '7f99ff99', '7fcc6633', '7fcc00ff', '7fccffcc', '7fff0000', '7fff00ff', '7fffcc00', '7fffffff', '7fcc00ff', '7fff0099', '7f0066cc', '7fcc99ff', '7f660033']
f = urllib.urlopen("http://www.mapaeducativo.edu.ar/geoserver/tematicos/ows?service=WFS&=1.0.0&request=GetFeature&typeName=tematicos:p_originarios&maxFeatures=50&outputFormat=json")
jsonToKml.imprimirKML(f.read(), colores[random.randint(0, len(colores)-1)])
