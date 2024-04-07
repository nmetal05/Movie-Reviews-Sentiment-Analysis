import string
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords

def preprocess(text):
    # remove html tags such as <br />
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.get_text()
    # remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)
    # turn text into lowercase
    text = text.lower()
    #split text into an array of words
    words = text.split()
    # remove stopwords from the array
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)
