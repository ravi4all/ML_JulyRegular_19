import math
import random
import csv

def loadCsv(path):
    data = []
    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def str_to_float(dataset):
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            dataset[i][j] = float(dataset[i][j])


def minMax(dataset):
    minMaxData = []
    for i in range(len(dataset[0])): 
        col = [dataset[j][i] for j in range(len(dataset))]
        minMaxData.append([min(col), max(col)])
    return minMaxData

def normalization(minMaxData,dataset):
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            numer = dataset[i][j] - minMaxData[j][0]
            denom = minMaxData[j][1] - minMaxData[j][0]
            dataset[i][j] = numer/denom

def crossValidation(dataset,k=5):
    folds = []
    dataset_copy = list(dataset)
    fold_size = len(dataset) // k
    for i in range(k):
        fold = []
        while len(fold) < fold_size:
            index = random.randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        folds.append(fold)
    return folds

def predict(row,coef):
    x = coef[0]
    for i in range(len(row) - 1):
        x += coef[i+1] * row[i]
    return 1 / (1 + math.exp(-x))

def accuracy_score(actual,pred):
    count = 0
    for i in range(len(actual)):
        if actual[i] == pred[i]:
            count += 1
    return count/len(actual) * 100

def evaluateAlgorithm():
    pass

def stochasticGD(dataset,epochs,alpha):
    coef = [0] * len(dataset[0])
    for epoch in range(epochs):
        for row in dataset:
            pred = predict(row,coef)
            loss = pred - row[-1]
            coef[0] = coef[0] - alpha * loss
            for j in range(len(row)):
                coef[j+1] = coef[j+1] - alpha * loss * row[j]
    return coef

def logsiticRegression():
    pass


filename = "data.csv"
dataset = loadCsv(filename)
str_to_float(dataset)
minMaxData = minMax(dataset)
normalization(minMaxData,dataset)
#folds = crossValidation(dataset)


