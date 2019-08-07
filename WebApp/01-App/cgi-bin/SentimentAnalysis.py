import pandas as pd

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import LogisticRegression

df_1 = pd.read_csv('imdb_labelled.txt',sep='\t',header=None)
df_2 = pd.read_csv('amazon_cells_labelled.txt',sep='\t',header=None)
df_3 = pd.read_csv('yelp_labelled.txt',sep='\t',header=None)

df = pd.DataFrame()
df = df.append(df_1)
df = df.append(df_2)
df = df.append(df_3)

df.columns = ['Review','Sentiment']

def textProcessing(document):
    tokens = []
    for i in range(len(document)):
        tokens.append(word_tokenize(document['Review'].iloc[i].lower()))
    wordsList = []
    s_word = stopwords.words("english")
    s_word.extend([".","also"])
    for tokenList in tokens:
        words = []
        for token in tokenList:
            if token not in s_word:
                words.append(token)
        wordsList.append(words)
    wnet = WordNetLemmatizer()
    for i in range(len(wordsList)):
        for j in range(len(wordsList[i])):
            wordsList[i][j] = wnet.lemmatize(wordsList[i][j],pos='v')
    for i in range(len(wordsList)):
        wordsList[i] = ' '.join(wordsList[i])
    
    return wordsList

def train():

    wordsList = textProcessing(df)
    cv = CountVectorizer()
    vect = cv.fit_transform(wordsList)
    y = df['Sentiment']
    x_train,x_test,y_train,y_test = train_test_split(vect,y,test_size=0.25)

    reg = LogisticRegression()
    reg.fit(x_train, y_train)
    return reg, cv

def test(rev):
    reg,cv = train()
    test_df = pd.DataFrame({"Review":[rev]})
    wordsList = textProcessing(test_df)
    v = cv.transform(wordsList)
    pred = reg.predict(v)
    return pred