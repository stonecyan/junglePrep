def favoriteGenre(userSongs, songGenres):
	songsToGenre = {}
	for genre in songGenres:
		for song in songGenres[genre]:
			songsToGenre[song]=genre
	genreCount = {}
	for user in userSongs:
		genreCount[user]={}
		for song in userSongs[user]:
			genre = songsToGenre[song]
			if genre in genreCount[user]:
				genreCount[user][genre]+=1
			else:
				genreCount[user][genre]=1
	outputDict = {}
	for user in genreCount:
		maxValue = max(genreCount[user].values())
		outputDict[user] = []
		for key in genreCount[user]:
			if genreCount[user][key]==maxValue:
				outputDict[user].append(key)
	return outputDict
