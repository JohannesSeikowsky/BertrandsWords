### BertrandsWords
Simple command line vocabulary training based on words used by Bertrand Russell
in "History of Western Philosophy" - Version 0.1

#### How to use it
Clone repo, navigate to "bertrands_words" directory, 
run program using python3 - `python3 main.py`

#### How it works
Program shows you words used by Russell. One at a time. For each word you can either
show its meaning plus an example of the word in use, move to the next word or end
the program. That's it.

At the start you can set whether you want to see rarer or less rare words
by setting an interval. For instance, 99-100 would show you the rarest 1% of words
in terms of their usage in contemporary English.

#### Dependencies
No dependencies needed if you are fine with just "History of Western Philosophy".
If you want to expand to other books as inputs, you'll need nltk to run
the two processing scripts.

#### Possible plans
This is a crude version 0.1 so there are many things that can be improved.
And things that can be added. I haven't decided yet. Some ideas: 
- extend program so that other books can easily and dynamically be added as "input" books
- add vocabulary training features like "hot listing" interest words for instance
- ability to see a particular word in the sentence it was originally used in within the book
it "came from"
