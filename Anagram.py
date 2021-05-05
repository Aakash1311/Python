def anagram(wordOne, wordTwo):
	wordOne = wordOne.lower()
	wordTwo = wordTwo.lower()
	return sorted(wordOne) == sorted(wordTwo)

result= anagram("iceman", "cinema")	
print(result)