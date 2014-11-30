import connection as conn
import pyak as pk
import json
from config import Geos, Data
import time

def getNabes(path):

	with open(path, 'rt') as nabes:
		latlongs = json.loads(nabes.read())

	return latlongs	

latlongs = getNabes(Data._PATH_TO_NEIGHBORHOODS)
#latlongs = getNabes(Data._PATH_TO_TEST)

for k,v in latlongs.items():

	nabe_name = k
	borough = latlongs[k]['borough']
	nabe_latitude = latlongs[k]['geo'][0]
	nabe_longitude = latlongs[k]['geo'][1]


	location = pk.Location(nabe_latitude, nabe_longitude)
	yakk = pk.Yakker(None, location, False)
	yaks = yakk.get_yaks()

	for yak in yaks:

		comments = []
		these_comments = yak.get_comments()

		if these_comments:
			for this in these_comments:
				comments.append({"comment": this.comment, "time": this.time, "likes": this.likes})



		handle = yak.handle if yak.handle is not None else ''

		key     = {"message_id":yak.message_id}
		yak_doc = {"message_id":yak.message_id,
				   "likes":yak.likes, 
				   "text":yak.message, 
				   "date":yak.time, 
				   "geometry":[yak.latitude, yak.longitude],
				   "handle": handle,
				   "neighborhood": nabe_name,
				   "borough": borough,
				   "comments": comments}

		print "adding %s from %s, %s - with %s comments" % (yak_doc['text'], nabe_name, borough, len(comments))
		conn.collection.update(key, yak_doc, upsert=True)
	time.sleep(5)   #lets not upset anyone





