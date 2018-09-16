"""
Take all words from original book,
filter and process them, put outcome it its own file
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet 
from nltk.stem import WordNetLemmatizer


def preprocess(book_file_path, output_file_name):
	# read from original book
	with open(book_file_path, "r") as book:
		book = book.read().lower()
		book = book.decode('utf-8')

	# get all words in list
	list_of_words = word_tokenize(book)

	# filter out stopwords
	stop_words = set(stopwords.words("english"))

	filter_one = []
	for each in list_of_words:
		if each not in stop_words:
			filter_one.append(each)

	# filter out strings that have a number in them
	def hasNumerical(inputString):
		results = []
		for char in inputString:
			results.append(char.isdigit())
		return any(results)

	filter_two = []
	for each in filter_one:
		if not hasNumerical(each):
			filter_two.append(each)

	# filter out strings with three characters or less
	filter_three = []
	for each in filter_two:
		if len(each) > 3:
			filter_three.append(each)

	# lemmatize all words
	lem = WordNetLemmatizer()
	filter_four = []
	for each in filter_three:
		filter_four.append(lem.lemmatize(each))

	# filter out those words that don't occur in the English dictionary
	# get all english words
	english_words = nltk.corpus.words.words()
	english_words_lower = []
	for each in english_words:
		english_words_lower.append(each.lower())

	# get intersection
	english_words_lower = set(english_words_lower)
	filter_four = set(filter_four)
	book_words = english_words_lower.intersection(filter_four)

	# write output to file
	with open(output_file_name, "w") as file:
		for each in book_words:
			each = each.encode("utf-8")
			file.write(each)
			file.write("\n")