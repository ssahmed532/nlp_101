#
# Tested using nltk 3.5
#
# Code is based on the following article:
#
# https://realpython.com/nltk-nlp-python/
#

import text_samples
import utils


ne_set = utils.extract_ne(text_samples.war_of_the_worlds_quote)
if ne_set:
    print(ne_set)
else:
    print("WARNING: Unable to extract any Named Entities from War of the Worlds quote text sample")
print(2 * '\n')

ne_set = utils.extract_ne(text_samples.dune_quote)
if ne_set:
    print(ne_set)
else:
    print("WARNING: Unable to extract any Named Entities from dune quote text sample")
print(2 * '\n')

ne_set = utils.extract_ne(text_samples.lotr_quote)
if ne_set:
    print(ne_set)
else:
    print("WARNING: Unable to extract any Named Entities from LoTR quote text sample")
print(2 * '\n')

ne_set = utils.extract_ne(text_samples.cto_connection_email)
if ne_set:
    print(ne_set)
else:
    print("WARNING: Unable to extract any Named Entities from CTO Connection Email text sample")
print(2 * '\n')
