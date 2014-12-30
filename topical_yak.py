from config import Data
import connection as conn
import sys, os

dirpath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dirpath + '/../MITIE/mitielib')

from mitie import *

try:
	_BORO = sys.argv[1] 
except:
	_BORO = 'ALL'
	print "You can specify a Borough: Brooklyn, Manhattan, Queens, Bronx, Staten Island"

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


	yaks_in_lists = [yak.lower().split() for yak in whichYaks(allYaks, boroYaks)]

	return yaks_in_lists


def generateTopics(text):
	ner = named_entity_extractor('../MITIE/MITIE-models/english/ner_model.dat')
	tokens = tokenize(text)
	entities = ner.extract_entities(tokens)

	print "\nEntities found: ", entities
	print "\nThis many entitites: ", len(entities)

	for e in entities:
		range = e[0]
		tag = e[1]
		entity_text = " ".join(tokens[i] for i in range)
		print "   " + tag + ": " + entity_text

def makeCorpus(yaks):
	txt = ""

	for y in yaks:
		txt += (" ").join(y).encode('utf-8').strip()

	return txt





if __name__ == '__main__':
	print "getting topics for", _BORO

	yaksLoad = getYaks(_BORO)

	yaks_dot_txt = makeCorpus(yaksLoad)

	generateTopics(yaks_dot_txt)


