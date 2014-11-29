import connection as conn
import pyak as pk
import json
from config import Geos, Data
import time

with open(Data._PATH_TO_NEIGHBORHOODS, 'rt') as nabes:
	latlongs = json.loads(nabes.read())

	for k,v in latlongs.items():

		nabe_name = k
		borough = latlongs[k]['borough']
		nabe_latitude = latlongs[k]['geo'][0]
		nabe_longitude = latlongs[k]['geo'][1]


	location = pk.Location(nabe_latitude, nabe_longitude)
	yakk = pk.Yakker(None, location, False)
	yaks = yakk.get_yaks()

	for yak in yaks:

		handle = yak.handle if yak.handle is not None else ''

		key     = {"date":yak.time}
		yak_doc = {"likes":yak.likes, 
				   "text":yak.message, 
				   "date":yak.time, 
				   "geometry":[yak.latitude, yak.longitude],
				   "handle": handle,
				   "neighborhood": nabe_name,
				   "borough": borough}

		print "adding %s from %s, %s" % (yak_doc['text'], nabe_name, borough)
		conn.collection.update(key, yak_doc, upsert=True)
	time.sleep(15)   #lets not upset anyone





