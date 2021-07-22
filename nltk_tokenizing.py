#
# Tokenizing text into sentences and words using the tokenizers
# available in NLTK.
#
# Tested using nltk 3.5
#
# Code is based on the following article:
#
# https://realpython.com/nltk-nlp-python/
#

import nltk
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus   import stopwords


TRIM_WHITESPACES = True



sample_text1 = """
Muad'Dib learned rapidly because his first training was in how to learn.
And the first lesson of all was the basic trust that he could learn.
It's shocking to find how many people do not believe they can learn,
and how many more believe learning to be difficult.
"""


sample_text2 = """
Hi Salman,


I'll keep this one short and sweet.


I noticed you haven't checked out CTO Connection. If it's not a good fit for you, no problem -- either way, you won't hear from me about it again.


But just in case you've missed the last couple of emails, I'll give it one last shot.


I built CTO Connection to be the premier place for CTOs and senior engineering leaders to connect and learn. It's packed full of interviews with CTOs from large organizations and start-ups alike, covering a wide range of topics from onboarding and managing remote teams to incident response.


Registration is completely free and once inside, you can register to attend any of our upcoming free online summits as well as catch replays of previous events, and we have big plans for the future, including the ability to join groups to network with other senior engineering leaders where you are or based on your interests or biggest challenges.


Interested in checking it out? https://www.ctoconnection.com/


All the best!

Peter


P.S. If you have any questions, please hit reply and let me know. I'd love to chat. If you're not interested, once again, apologies for taking up space in your inbox.


Peter Bell

Founder and CTO, CTO Connection
"""


# Worf quote
sample_text3 = "Sir, I protest. I am not a merry man!"


def print_tokens(token_list):
    print("There are {} tokens".format(len(token_list)))

    for index, token in enumerate(token_list, start=1):
        if TRIM_WHITESPACES:
            token = token.strip()
        print("{}: {}".format(index, token))


# tokenize into sentences
tokens1 = sent_tokenize(sample_text1)
print_tokens(tokens1)
print("sample_text1 has {} sentences in it".format(len(tokens1)))
print(3 * '\n')

# tokenize into sentences
tokens2 = sent_tokenize(sample_text2)
print_tokens(tokens2)
print("sample_text2 has {} sentences in it".format(len(tokens2)))
print(3 * '\n')


# tokenize into words
word_tokens1 = word_tokenize(sample_text1)
print_tokens(word_tokens1)
print("sample_text1 has {} words in it".format(len(word_tokens1)))
print(3 * '\n')

# tokenize into words
word_tokens2 = word_tokenize(sample_text2)
print_tokens(word_tokens2)
print("sample_text2 has {} words in it".format(len(word_tokens2)))
print(3 * '\n')


#nltk.download("stopwords")

STOP_WORDS = set(stopwords.words("english"))

print("Filtering stop words and punctuations from sample_text1...")
filtered_word_tokens1 = []
for word in word_tokens1:
    w = word.casefold()
    if (w not in STOP_WORDS) and (w not in string.punctuation):
        filtered_word_tokens1.append(word)
print("sample_text1 has {} *filtered* words in it".format(len(filtered_word_tokens1)))
print_tokens(filtered_word_tokens1)
print(3 * '\n')

print("Filtering stop words and punctuations from sample_text2...")
filtered_word_tokens2 = []
for word in word_tokens2:
    w = word.casefold()
    if (w not in STOP_WORDS) and (w not in string.punctuation):
        filtered_word_tokens2.append(word)
print("sample_text2 has {} *filtered* words in it".format(len(filtered_word_tokens2)))
print_tokens(filtered_word_tokens2)
print(3 * '\n')
