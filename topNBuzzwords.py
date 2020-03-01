import heapq
import re

#O(NlogK)
def topNBuzzwords(numToys, topToys, toys, numQuotes, quotes):
	#toy:[count, quoteCount]
	toysFreq = {}
	toysHeap = []
	for toy in toys:
		toysFreq[toy]=[0,0]
	for quote in quotes:
		quoteToy = {}
		for toy in toys:
			quoteToy[toy]=False
		quoteWords = quote.lower().split()
		for word in quoteWords:
			word = re.sub('[^a-z]',"", word)
			if word in toysFreq:
				toysFreq[word][0]+=1
				if quoteToy[word]==False:
					quoteToy[word]=True
					toysFreq[word][1]+=1
	for toy in toysFreq:
		t = [toysFreq[toy][0], toysFreq[toy][1], toy]
		heapq.heappush(toysHeap, t)
		if len(toysHeap)>topToys:
			heapq.heappop(toysHeap)
	output = []
	for i in toysHeap:
		output.append(i[2])
	return(output[::-1])


numToys = 6
topToys = 2
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
numQuotes = 6
quotes = [
"Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
"The new Elmo dolls are super high quality",
"Expect the Elsa dolls to be very popular this year, Elsa!",
"Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
"For parents of older kids, look into buying them a drone",
"Warcraft is slowly rising in popularity ahead of the holiday season"
];
print(topNBuzzwords(numToys, topToys, toys, numQuotes, quotes))
