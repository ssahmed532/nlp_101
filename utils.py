import nltk
from nltk.tokenize import sent_tokenize, word_tokenize


def extract_ne(quote, lang='english'):
    words = word_tokenize(quote, language=lang)
    tags = nltk.pos_tag(words)
    tree = nltk.ne_chunk(tags, binary=True)

    return set(
        " ".join(i[0] for i in t)
        for t in tree
        if hasattr(t, "label") and t.label() == "NE"
        )
