import pandas as pd

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import pickle as pkl

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

def test(rev):
    file = open('model.pkl','rb')
    reg = pkl.load(file)
    file.close()

    file = open('cv.pkl','rb')
    cv = pkl.load(file)
    file.close()

    test_df = pd.DataFrame({"Review":[rev]})
    wordsList = textProcessing(test_df)
    v = cv.transform(wordsList)
    pred = reg.predict(v)
    return pred