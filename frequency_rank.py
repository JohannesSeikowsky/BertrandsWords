"""
Take preprocessed words of the book from file,
frequency rank them, put outcome it its own file
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet 
from nltk.stem import WordNetLemmatizer


def frequency_rank(input_file, output_file):
	# get bertrands words
	with open(input_file, "r") as f:
		book_words = f.readlines()

	book_words_list = []
	for each in book_words:
		book_words_list.append(each.replace("\n", ""))

	# get english words - ascending in terms of their frequency in use
	with open("word_frequencies.txt", "r") as f:
		english_words = f.readlines()

	english_words_list = []
	for each in english_words:
		english_words_list.append(each.replace("\n", ""))

	# get intersection of bertrands words and english
	bertrands_words_set = set(book_words_list)
	english_words_set = set(english_words_list)
	intersection = bertrands_words_set.intersection(english_words_set)

	# rank according to frequency 
	# essentially by using fact that frequency file is ranked in ascending order of frequency
	indexes = []
	for word in intersection:
		word_index = english_words_list.index(word)
		indexes.append(word_index)

	sorted_indexes = sorted(indexes, key=int)

	words_in_order = []
	indexed_words_in_order = []
	for each in sorted_indexes:
		words_in_order.append(english_words_list[each])
		indexed_words_in_order.append((english_words_list[each], each))

	# write to file in order of frequency for repeated retrieval 
	with open(output_file, "w") as f:
		for each in words_in_order:
			try:
				each = each.encode("utf-8")
				f.write(each)
				f.write("\n")
			except:
				pass