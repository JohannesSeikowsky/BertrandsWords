import os, random, requests, json

""" 
	Simple command line vocabulary training based on words used by Bertrand Russel,
	specifically in "History of Western Philosophy".
"""

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
	# asking user which "rarity" interval he'd like to see
	preffered_interval = raw_input("Set your preffered level of 'rarity' for the words you'll see. \n For Example: \n 90-100 --> rarest 10% of words \n 70-100 --> rarest 30% of words  \n 0-20 --> most common 25% \n")
	
	# setting default of 20% rarest words
	if preffered_interval is "":
		preffered_interval = "80-100"

	interval = preffered_interval.split("-")
	lower_bound, upper_bound = interval[0], interval[1]

	# computing boundaries
	amount_of_words = 9733 # 9733 is the total amount of words extracted from the book
	lower_bound = amount_of_words // 100 * int(lower_bound)
	upper_bound = amount_of_words // 100 * int(upper_bound)

	# getting words from the specific interval set by the user
	relevant_lines = []
	with open('bertrands_words_ranked.txt') as f:
		for i, line in enumerate(f):
			if i > lower_bound and i < upper_bound:
				relevant_lines.append(line.strip())


	# continued command line interaction
	next_command = "n"
	while next_command is not "x":

		if next_command is "n":
			print "-------------------------------------------" + "\n" + "\n"
			chosen_word = random.choice(relevant_lines)
			print chosen_word

			print "\n" + "\n" + "n - next | m - show meaning | x - exit"
			next_command = raw_input("Action: ")
		
		elif next_command is "m":
			# print meaning
			print "-------------------------------------------"
			try:
				
				response = requests.get("https://owlbot.info/api/v2/dictionary/" + chosen_word)
				response = json.loads(response.text)
				print chosen_word + " - " + response[0]["definition"]
				print "example" + " - " + str(response[0]["example"])

				"""
					# nltk wordnet alternative for getting word meanings
					from nltk.corpus import wordnet 
					syns = wordnet.synsets(chosen_word)
					print chosen_word + " - " + syns[0].definition()
				"""
			except Exception as e:
				print "Nothing found for this word. Sorry. Try another."

			print "\n" + "\n" + "n - next | x - exit"
			next_command = raw_input("Action: ")
		else:
			break


"""
- leave all scripts in (easiest for users) // they dont care about the preprocessing
- use api instead of wordnet - again because easiest for users
- basic readme
- push
"""