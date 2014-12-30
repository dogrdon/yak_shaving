from config import Data
import connection as conn
import sys

try:
	_BORO = sys.argv[1] 
except:
	_BORO = 'ALL'

def getYaks(*args):

	def whichYaks(a, b):
		if len(b) == 0:
			return a
		else:
			return b

	boro = args[0]

	allYaks = [] 
	boroYaks = []

	res = conn.collection.find()


	for r in res:
		if boro != 'ALL' and r['borough'].lower() == boro.lower():
			boroYaks.append(r['text'])
		else:
			allYaks.append(r['text'])


	yaks_corpus = [yak.lower().split() for yak in whichYaks(allYaks, boroYaks)]

	return yaks_corpus





if __name__ == '__main__':
	allYaks = getYaks(_BORO)
	print len(allYaks)