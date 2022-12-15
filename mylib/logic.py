import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """Wikipedia fetcher"""

    mywiki = wikipedia.summary(name, length)
    return mywiki

def search_wiki(name):
    """Search wikipedia for names"""
    results = wikipedia.search(name)
    return results

def phrases(name):
    """Returns phrases from wikipedia"""
    page = wiki(name)
    blob = TextBlob(name)
    phrases = blob.noun_phrases
    return phrases


