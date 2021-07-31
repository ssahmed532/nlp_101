# Some basic NLP operations & tasks using the NLTK library
# 
# Code below is based on the following RealPython article:
#
#       https://realpython.com/python-nltk-sentiment-analysis/
#

import nltk
import string

from nltk.tokenize import word_tokenize
import text_samples


LANG_ENGLISH = "english"
STOP_WORDS = set(nltk.corpus.stopwords.words(LANG_ENGLISH))
print(f"Loaded {len(STOP_WORDS)} English language stop words")

words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]
print(f"Number of words from State of Union corpus: {len(words)}")
#print(words)

# Since all words in the STOP_WORDS set are lowercase, and those in the original
# list may not be, use str.lower() to account for any discrepancies. Otherwise,
# we may end up with mixedCase or capitalized stop words still in our list.
filtered_words = [w for w in words if w.lower() not in STOP_WORDS]
print(f"Number of words after filtering for stop words: {len(filtered_words)}")

filtered_words2 = []
word_tokens: list[str] = nltk.word_tokenize(text_samples.cto_connection_email)
for word in word_tokens:
    w = word.casefold()
    if w.isalpha() and (w not in STOP_WORDS) and (w not in string.punctuation):
        filtered_words2.append(word)
print(filtered_words2)

# Frequency Distribution
freq_dist = nltk.FreqDist(filtered_words2)
print(freq_dist.most_common(5))
print(freq_dist.tabulate(10))
print(2 * '\n')

# recompute the frequency distribution but normalize all words to lowercase
freq_dist_lower = nltk.FreqDist([w.lower() for w in filtered_words2])
print(freq_dist.most_common(5))
print(freq_dist.tabulate(10))
print(2 * '\n')

# Concordance
text = nltk.Text(word_tokens)
print(text.concordance("CTO", lines=5))
print(2 * '\n')
print(text.concordance("leaders", lines=5))
print(2 * '\n')

concordance_list = text.concordance_list("CTO", lines=5)
for entry in concordance_list:
    print(entry.line)
print(2 * '\n')

words: list[str] = nltk.word_tokenize(text_samples.pep20_zen_of_python)
text = nltk.Text(words)
freq_dist = text.vocab() # Equivalent to freq_dist = nltk.FreqDist(words)
print(freq_dist.tabulate(10))
print(2 * '\n')

# Collocations
words = [w for w in nltk.corpus.state_union.words() if w.isalpha()]
finder = nltk.collocations.TrigramCollocationFinder.from_words(words)
print(finder.ngram_fd.most_common(5))
print(finder.ngram_fd.tabulate(5))
