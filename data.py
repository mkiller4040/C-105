import math, csv, pandas

# with open('data.csv', newline = '') as f :
#     reader = csv.reader(f)
#     datalist = list(reader)

# data = []

# for j in datalist :
#     data.append(int(datalist[j]))

datalist = pandas.read_csv("data.csv")

def calcMean(data) :
    dataLength = 10
    dataSum = 0

    for i in data :
        # i = str(i)
        dataSum = dataSum + int(i)

    mean = dataSum/dataLength

    return mean

def calcSTD(data) :
    squaredData = []
    for d in data :
        # d = str(d)
        meanDifference = int(d) - calcMean(datalist)
        meanDifferenceSq = meanDifference**2
        squaredData.append(meanDifferenceSq)
    
    squaredDataSum = 0

    for d in squaredData :
        squaredDataSum = squaredDataSum + d

    STD = math.sqrt((squaredDataSum/9))

    return STD

print("The Standard Deviation of the dataset is :", calcSTD(datalist))