 def suggestedProducts(products, searchWord):
        suggestedOutput = []
        searchPhrase = ""
        products.sort()
        for letter in searchWord:
            searchPhrase+=letter
            suggestedOutput.append([])
            outputIndex = len(suggestedOutput)-1
            for word in products:
                if word[:len(searchPhrase)]==searchPhrase:
                    suggestedOutput[outputIndex].append(word)
                if len(suggestedOutput[outputIndex])==3:
                    break
        return suggestedOutput
