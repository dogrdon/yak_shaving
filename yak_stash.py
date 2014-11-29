import connection as conn
import pyak as pk
from config import Geos


location = pk.Location(Geos._LATITUDE, Geos._LONGITUDE)
yakk = pk.Yakker(None, location, False)
yaks = yakk.get_yaks()

for yak in yaks:

	handle = yak.handle if yak.handle is not None else ''

	key     = {"date":yak.time}
	yak_doc = {"likes":yak.likes, 
			   "text":yak.message, 
			   "date":yak.time, 
			   "geometry":[yak.latitude, yak.longitude],
			   "handle": handle}

	print "adding", yak_doc['text']
	conn.collection.update(key, yak_doc, upsert=True)    



