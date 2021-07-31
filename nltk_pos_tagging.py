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


words = word_tokenize(text_samples.carl_sagan_quote)
print("Word tokens:")
print(words)
print(2 * '\n')

tagged_words = nltk.pos_tag(words)
print("Tagged words:")
print(tagged_words)
print(2 * '\n')

words_in_excerpt = word_tokenize(text_samples.jabberwocky_excerpt)
tagged_words_in_excerpt = nltk.pos_tag(words_in_excerpt)
print("Tagged words in Jabberwocky excerpt:")
print(tagged_words_in_excerpt)
print(2 * '\n')
