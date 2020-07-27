# conda install nltk
# NLM using NLTK
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
# pull from website
url = 'https://www.gutenberg.org/files/11/11-h/11-h.htm'
# assign r
r = requests.get(url)
#
type(r)
# Looking for return of
# Requests.models.Response
# Convert text to soup
html = r.text
soup = BeautifulSoup("html.parser")
type(soup)
# Expecte return of
# bs4.BeautifulSoup
# HTML tags to extract
soup.title.string
# Returns title from website
# 'The Count of Monte Cristo, by Alexandre Dumas, pÃ¨re'
#
text = soup.get_text()
tokenizer = RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(text)
tokens[:5]
# Tokenized results returned.
# Remove capitialized words because it is not needed.
words = []
for word in tokens:
    words.append(word.lower())
words[:5]
# Returns
# ['the', 'count', 'of', 'monte', 'cristo']
# Remove stop words
# Add Python stop words using Terminal for first use, python -m nltk.downloader stopwords
stopwords = nltk.corpus.stopwords.words('english')
#
stopwords[:10]
# Returns
# ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're"]
#
wordsWithoutStops = []
for word in words:
    if word not in stopwords:
        wordsWithoutStops.append(word)
# Search words without stop words
wordsWithoutStops[:5]
# Should return
# ['count', 'monte', 'cristo', 'alexandre', 'dumas']
# Plot data
sns.set()
frequencyDis = nltk.FreqDist(wordsWithoutStops)
frequencyDis.plot(25)















