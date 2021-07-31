#
# Tested using nltk 3.5
#
# Code is based on the following article:
#
# https://realpython.com/nltk-nlp-python/
#

import nltk
import text_samples
from nltk.tokenize import word_tokenize


words_in_lotr_quote = word_tokenize(text_samples.lotr_quote)
print("Words in LOTR quote:")
print(words_in_lotr_quote)


lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)
print("LOTR quote POS tags:")
print(lotr_pos_tags)


ner_tree = nltk.ne_chunk(lotr_pos_tags)
ner_tree.draw()
