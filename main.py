"""
BertrandsWords - Simple command line vocabulary training based on words used by Bertrand Russel,
specifically in his book "History of Western Philosophy".

General structure:
The original book from which all words are taken is in the "History_of_Western_Philosophy.txt" file.
If processing of the book has not been done, this is the first thing that the program does.
The main functions that do this processing are in the "preprocess_book" and the "frequency_rank" modules
respectively. The "preprocess_book" module gets all words out in the first place, filters them in
various ways and reduces them to their "base word" (lemmatizes them). The "frequency_rank" module
ranks those words in terms of their frequency based on the "english language frequncy ranking" which you 
can find in the word_frequencies.txt file. This frequency ranking is so that users can set how "rare" 
the words they'll see ought to be, like let's say the rarest 1% of words or the rarest 10%.

If the processing has been done and the program gets run, the user can interact with the 
program on the command line. In the code below this is the "command line interaction layer".
"""

import os, random, requests, json


files_in_dir = os.listdir('.')

# do processing if required
if "bertrands_words_ranked.txt" not in files_in_dir:
	# get all words from book
	from preprocess_book import preprocess
	preprocess("History_of_Western_Philosophy.txt", "bertrands_words.txt")

	# frequency rank those words
	from frequency_rank import frequency_rank
	frequency_rank("bertrands_words.txt", "bertrands_words_ranked.txt")

# command line interaction layer
else:
	# ask user which "rarity" interval he'd like to see
	preffered_interval = input("Set your preffered level of 'rarity' for the words you'll see. \n For Instance: \n 90-100 --> rarest 10% of words \n 70-100 --> rarest 30% of words  \n 0-20 --> most common 25% \n")
	
	# set default of 20% rarest words
	if preffered_interval is "":
		preffered_interval = "80-100"

	interval = preffered_interval.split("-")
	lower_bound, upper_bound = interval[0], interval[1]

	# compute boundaries
	amount_of_words = 9733 # total amount of words extracted from book
	lower_bound = amount_of_words // 100 * int(lower_bound)
	upper_bound = amount_of_words // 100 * int(upper_bound)

	# get words from the specific interval set by the user
	relevant_lines = []
	with open('bertrands_words_ranked.txt') as f:
		for i, line in enumerate(f):
			if i > lower_bound and i < upper_bound:
				relevant_lines.append(line.strip())


	# continued command line interaction
	next_command = "n"
	while next_command is not "x":
		# display a word to user
		if next_command is "n":
			print("-------------------------------------------" + "\n" + "\n")
			chosen_word = random.choice(relevant_lines)
			print(chosen_word)

			print("\n" + "\n" + "n - next | m - show meaning | x - exit")
			next_command = input("Action: ")

		# print meaning of a word		
		elif next_command is "m":
			print("-------------------------------------------")
			try:
				response = requests.get("https://owlbot.info/api/v2/dictionary/" + chosen_word)
				response = json.loads(response.text)
				print(chosen_word + " - " + response[0]["definition"])
				print("example" + " - " + str(response[0]["example"]))

				"""
					# nltk wordnet alternative for getting word meanings
					from nltk.corpus import wordnet 
					syns = wordnet.synsets(chosen_word)
					printchosen_word + " - " + syns[0].definition()
				"""
			except Exception as e:
				print("Nothing found for this word. Sorry. Try another.")

			print("\n" + "\n" + "n - next | x - exit")
			next_command = input("Action: ")
		# exit command line session
		else:
			break