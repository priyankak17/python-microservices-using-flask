import wikipedia


def wiki(name="War Goddess", length=1):
    """Wikipedia fetcher"""

    mywiki = wikipedia.summary(name, length)
    return mywiki
