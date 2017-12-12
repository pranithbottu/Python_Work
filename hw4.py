"""
======================================================================
Homework 4

Released: 2017-10-17
Due Date: 2017-10-24, EoD

They told me I could be anything...
...so I became void*.
======================================================================
"""

# is unique
def is_unique(word):
	"""
	Given a string, return true if the string's characters are unique.

	Args:
		(str) word: the input string.
	
	Returns:
		(bool) True if the string's characters are unique, False otherwise.
	"""
	return (len(word) == len(set(word)))


# Counting Anagrams
def count_anagrams(arr, uniq):
	"""
	Given a list of strings, returns the exact anagrams of uniq in the list.
	
	Args:
		(List[str]) arr:  a list of strings.
		(str)       uniq: a string.
	
	Returns:
		(int) the number of anagrams of uniq in arr.
	"""
	count = 0
	for i in range(0, len(arr)):
		if sorted(arr[i].lower()) == sorted(uniq):
			count+=1
	return count


# Anagram of Palindrome
def anagram_of_palindrome(word):
	"""
	Given a string, return true if the string is an anagram of a palindrome.

	Args:
		(str) word: the input string
	
	Returns:
		(bool) whether or not the input string is an anagram of a palindrome.
	"""
	characters = sorted(word)
	charCounts = []
	for i in range(0, len(characters)):
		count = 0
		for j in range(0, len(word)):
			if characters[i] == word[j]:
				count+=1
		charCounts.append(count)
	countOdd = 0
	for i in range(0, len(charCounts)):
		if (charCounts[i]%2) == 1:
			countOdd+=1
	if countOdd > 1:
		return False
	else:
		return True


# Reverse Dictionary
def reverse_dictionary(d):
	"""
	Given a dictionary d, reverse its keys and values.
	The values will all be unique.
	
	Args:
		(Dict[Any, Any]) d: the dictionary.

	Returns:
		(Dict[Any, Any]) a dictionary where the keys of d are its values and vice-versa. 
	"""
	revDict = {j:i for i, j in d.items()}
	return revDict


# Alphabet Finder
def alphabet_finder(sentence):
	"""
	Given a string, returns the shortest substring that:
		1. starts from the beginning of the string
		2. contains all the letters of the alphabet (case insensitive)
	If this is never true, return None.
	
	Args:
		(str) sentence: the input string

	Returns:
		(str) the shortest substring of sentence that satisfies both (1) and (2).
	"""
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	if len(sentence) == 26:
		if alphabet in sentence:
			return sentence
	else:
		indexArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		countArray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		alphaArray = sorted(alphabet)
		for i, j in enumerate(sentence):
			for k in range(0, len(alphaArray)):
				if alphaArray[k] == j:
					countArray[k] += 1
					if countArray[k] < 2:
						indexArray[k] = i + 1
		return sentence[:max(indexArray)]


# Happy Numbers
def happy_numbers(n):
	"""
	Given n, return the number of happy numbers between 1 and n (inclusive).
	https://en.wikipedia.org/wiki/Happy_number

	Args:
		(int) n: the upper bound.
	
	Returns:
		(int) the number of happy numbers from 1 to n.
	"""
	pass
