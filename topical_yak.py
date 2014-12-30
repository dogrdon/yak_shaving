from config import Data
import connection as conn

def getYaks(*args):

	yaks = []

	res = conn.collection.find()

	for r in res:
		yaks.append(r['text'])

	yaks_corpus = [yak.lower().split() for yak in yaks]

	return yaks_corpus





if __name__ == '__main__':
	allYaks = getYaks()
	print allYaks