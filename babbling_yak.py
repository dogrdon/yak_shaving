from config import Data
import connection as conn
import random
import json

'''To construct [an order 1 model] for example, 
   one opens a book at random and selects a letter at random on the page. 
   This letter is recorded. The book is then opened to another page and one reads 
   until this letter is encountered. The succeeding letter is then recorded. 
   Turning to another page this second letter is searched for and the succeeding letter 
   recorded, etc. It would be interesting if further approximations could be constructed, 
   but the labor involved becomes enormous at the next stage. -Claude Shannon'''


def getYaks(*args):
	'''gets yaks from datastore and creates a list of word lists for each
	pass query arguments if you want to narrow things down a bit'''
	yaks = []

	res = conn.collection.find()

	for r in res:
		yaks.append(r['text'])

	yaks_corpus = [yak.split() for yak in yaks]

	return yaks_corpus


def orderOneRamble(wordlist):

	sentence_words = []

	count = 0

	word = ''

	while count < random.randrange(15, 21):


		if word == '':
			sentence = wordlist[random.randrange(0, len(wordlist))]
			word = sentence[random.randrange(0, len(sentence))].title()
			sentence_words.append(word)
			count+=1
		else:
			sentence = wordlist[random.randrange(0, len(wordlist))]

			if word in sentence and (sentence.index(word) + 1) <= (len(sentence) - 1):
				word = sentence[sentence.index(word) + 1]
				sentence_words.append(word) 
				count += 1
			else:
				continue

	sillySentence = ' '.join(sentence_words)

	return sillySentence

if __name__ == '__main__':
	allYaks = getYaks()
	print orderOneRamble(allYaks)


