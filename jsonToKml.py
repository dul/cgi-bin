import string
import os
import json
#~ {"type":"Feature","id":"p_originarios.fid-45f738db_13dfe6a3989_636",
#~ "geometry":{"type":"MultiPolygon","coordinates":[[[[-7508113.476286065,-7169165.809313639],
#~ [-7492287.42678002,-7183923.9024039665],[-7461961.55363706,-7199755.045558206],
#~ [-7459544.398016638,-7209172.557110039],[-7465902.669459352,-7235580.286207172],
#~ [-7473355.344484281,-7247461.155298464],[-7469298.195032114,-7261688.98375237],
#~ [-7460031.719369557,-7273005.44156396],[-7449516.766099904,-7289514.848322037],
#~ [-7448035.400538539,-7308092.961847546],[-7449077.692495803,-7321919.06432386],
#~ [-7437980.77591145,-7333319.291574334],[-7435065.724614975,-7343329.548489667],
#~ [-7446335.130202428,-7344062.039618168],[-7465795.317242355,-7342053.195453303],
#~ [-7483013.206119622,-7336131.617160807],[-7499772.447742343,-7330185.203672737],
#~ [-7500932.721584416,-7323231.831097441],[-7499680.891760656,-7303365.1617559455],
#~ [-7496569.546012151,-7275833.878065837],[-7499340.455493993,-7263739.408207024],
#~ [-7503009.8891518,-7254219.251159768],[-7505642.710651046,-7236160.984773054],
#~ [-7505845.227054847,-7225031.2584068645],[-7508681.213306665,-7217707.321622311],
#~ [-7512708.231355867,-7206523.580824059],[-7510599.765838399,-7186967.873787248],
#~ [-7508113.476286065,-7169165.809313639]]]]},
#~ "geometry_name":"the_geom","properties":{"gid":639,"valor":"ONA","valor2":"ONA"}},



def imprimirKML(texto, color):
	dic = json.loads(texto)
	features = dic["features"] #lista de dicts, cada dic tiene un dic (key geometry) con un poligino
	print 'Content-Type: application/vnd.google-earth.kml+xml'
	print
	print('<?xml version="1.0" encoding="UTF-8"?>')
	print('<kml xmlns="http://earth.google.com/kml/2.2">')
	print('<Document>')
	print('\t<name> Cochabambas</name>')
	print('\t<Folder>')
	print('\t\t<name>Cochabambitas</name>')
	for i in features:
		print('\t\t<Placemark>')
		print('\t\t\t<name>polygon'+str(i['id'])+'</name>')
		dicPol = i["geometry"] #dict con el poligono
		if dicPol['type'] == "MultiPolygon":
			print('\t\t\t<Polygon>')
			print('\t\t\t\t<outerBoundaryIs>')
			print('\t\t\t\t\t<LinearRing>')
			print('\t\t\t\t\t\t<coordinates>')
			
			coords = dicPol['coordinates'][0][0]
			for e in coords:
				print('\t\t\t\t\t\t\t'+str(e[0])+','+str(e[1])+',0')
			
			print('\t\t\t\t\t\t</coordinates>')
			print('\t\t\t\t\t</LinearRing>')
			print('\t\t\t\t</outerBoundaryIs>')
			print('\t\t\t</Polygon>')
			#~ STYLE 
			print('\t\t\t<Style>')
			print('\t\t\t\t<PolyStyle>')
			print('\t\t\t\t\t<color>ffffffff</color>')
			print('\t\t\t\t\t<colorMode>random</colorMode>')
			print('\t\t\t\t</PolyStyle>')
			print('\t\t\t</Style>')

		print('\t\t</Placemark>')
	print('\t</Folder>')
	print('</Document>')
	print('</kml>')
