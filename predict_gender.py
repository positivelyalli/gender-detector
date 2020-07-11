import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import TweetTokenizer
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import text 



def split(x):
    if "'" in x:
        y = x.split("'")[0]
    else:
        y = x
    return y


def init():
    stemmed = pd.read_csv('data/final.csv')
    stemmed = stemmed.fillna('')
    
    dialogue = stemmed.dialogue.to_list()
    vec = CountVectorizer(max_features = 1000)
    vecf = vec.fit(dialogue)
    
    vector = vecf.transform(dialogue).toarray()
    x = vector
    y = stemmed.iloc[:,1].values
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.1, random_state = 42)
    
    nb = MultinomialNB()
    nb.fit(x_train,y_train)
    return nb, vecf


def predict_gender(t):
    print('line 40' + t)
    nb, vecf = init()

    character = pd.read_csv('data/fixed_characters.csv')
    sw = stopwords.words('english')
    names = character.name.str.lower().to_list()
    sw.extend(names)
    print(t)
    tknzr = TweetTokenizer()
    text_tokens = tknzr.tokenize(t)
    text_tokens = [split(x) for x in text_tokens]
    tokens_without_sw = [word for word in text_tokens if not word in sw]
    lemma = nltk.WordNetLemmatizer()
    description = [lemma.lemmatize(word) for word in tokens_without_sw]
    words = " ".join(description)
    words = [words]
    
    test_x = vecf.transform(words).toarray()
    test_y = nb.predict(test_x)
    if test_y[0] == 0:
        gender = 'Male'
    else:
        gender = 'Female'
    return gender





    