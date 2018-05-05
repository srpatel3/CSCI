import os
import pandas as pd
import math
import Mark1
import Mark2
import string
import operator
import random
from nltk.tokenize import word_tokenize as tokens
def getDict(readFile,temp):
    for line in readFile:
        line = line.translate(None, string.punctuation)
        line = line.lower()
        line = tokens(line)
        if len(line) != 0:
            for word in line:
                if not temp.has_key(word):
                    temp[word] = 1
                else:
                    temp[word] += 1
            # print line
def getBoW(path):
    try:
#        print "In getBo"
        fileToread = open(path,"r")
        bow = []
        for line in fileToread:
            line = line.translate(None, string.punctuation)
            line = line.lower()
            line = tokens(line)
    #        line = line.split(" ")
            if not len(line) == 0:
                bow.extend(line)
    #        print line
        return bow
    except Exception as e:
        print e

def getDistance(firstList,secondList):
    sum1 = 0
    for word in firstList:
        sum1 = sum1 + math.pow((firstList[word]- secondList[word]),2)
#    print sum1
    return sum1
def getCluster(item,listTFIDF,centSet):
    listTotal = []
    dist = 0
#    print centSet[0]
    for centroid in centSet:
        dist = getDistance(centroid,listTFIDF[item])
        listTotal.append(dist)
    return listTotal.index(min(listTotal))

# Actually implementing K Means
def KMeans(k1,listTFIDF,clusters,k):
    centSet =[]
    centSetHave = []
    remSet = set()

    for i in range(len(listTFIDF)):
        remSet.add(i)

    for i in k:
        centSetHave.append(i)

    for tempset in centSetHave:
        remSet = remSet.difference(set({tempset}))
#    print "hi"
    for item in remSet:
        index = getCluster(item, listTFIDF,k1)
#        print index
        clusters[index].add(item)
#    print clusters

    return clusters

# Actually implementing K Means
def KMeans1(k1,listTFIDF):
    centSet =[]
    centSetHave = []
    clusters = []
    remSet = set()
    for i in range(len(listTFIDF)):
        remSet.add(i)

    for i in range(0,len(k1)):
        clusters.append(set({}))
#    for tempset in centSetHave:
#        remSet = remSet.difference(set({tempset}))

    for item in remSet:
        index = getCluster(item, listTFIDF,k1)
#        print index
        clusters[index].add(item)

    return clusters

def updatedCentriods(clusters,listTFIDF):
    listCent = []
    for clustSet in  clusters:
        cent1  ={}
        for word in listTFIDF[0]:
            sum1 = 0
            for point in clustSet:
                sum1 = sum1 + listTFIDF[point][word]       
            avg = sum1/len(listTFIDF)
            cent1[word] = avg
        listCent.append(dict(cent1))
        cent1.clear()
    return listCent

def calculateSSE(centList,clusters,listTDIDF):    
    try:
        finSSE = 0
        for i in range(0,len(clusters)):
            cluster = clusters[i]
            cent = centList[i]
            intSSE = 0
            for item in cluster:
                intSSE = intSSE + getDistance(cent,listTDIDF[item])
#            print intSSE
            finSSE = finSSE + intSSE
        return finSSE
    except Exception as e:
        print e
        
def sortedDict(dictList):
#     print "Soreted"
     path = "C:\\Users\\srpatel3\\git\\Data_Files\\20news-18828\\"
     dirCount = {}
     try:   
         dirList = []
         for roots,dirs,files in os.walk(path):
             if not dirs == []:
                 dirList = dirs
         i = 0
         for item in dictList:
             dirCount[dirList[i]] = len(item)
             i += 1
         print dirCount
         
         dirCount = list(dirCount.iteritems())
         dirCount.sort(key=operator.itemgetter(1),reverse = True)
         print dirCount
         dirCount = dirCount[0:10]
         print dirCount
         dirlist = list(zip(*dirCount))[0]
#         for item in dirCount:
#                 dirlist.append(str(temp[0]) for temp in item)
#         print "Only Dir"
         return dirlist
     except Exception as e:
         print e.message
#    dictList = sorted(dir_Dict.items(), key=lambda x:x[1], reverse=True)
#     print dictLis
def getDictList():
#    print "In Another Dunf"
    path = "C:\\Users\\srpatel3\\git\\Data_Files\\20news-18828\\"
    try:
        dirList = []
        for roots,dirs,files in os.walk(path):
            if not dirs == []:
                dirList = dirs
#        fileList = []
        dictList = []
        for direct in dirList:
#            print direct
            temp = {}
            count = 0
            for roots,dirs,files in os.walk(path+direct):
                print "Processing Directory :" + str(count)
                count += 1
                if not files == []:
                    for fileName in files:
                        pathToFile = path+direct+"\\"+fileName               
                        print "Processing file  : " + pathToFile
                        fileToRead = open(pathToFile)
                        getDict(fileToRead,temp)
            dictList.append(temp)
#            break
        dictlist = []
        dictlist = sortedDict(dictList)
        return dictlist

    except Exception as e:
        print e

def main1():
     path = "C:\\Users\\srpatel3\\git\\Data_Files\\20news-18828\\"
     directory_Dicts = []
     dirList = []
     fileList = []
     try:
        print "Loading your Data"
        listBagOfWords = []
#        print "Here1"
        directory_Dicts = getDictList()
#        print "Here2"
        for item in directory_Dicts:
#            print "In For Loop"
            for roots,dirs,files in os.walk(path+"\\"+item):
#                print "Another Loop"
                for filename in files:
                    listBagOfWords.append(getBoW(path+"\\"+item+"\\"+filename))
        print "Now Processing Data..."
        listTDIDF = Mark1.documentClustering(listBagOfWords)
#        Mark2.calcDBScan(listTDIDF)
#        print listTDIDF[0]
        numOfk = 4
        k1 = []
        k = []
        clusters = []
        listofCent = random.sample(range(1, len(listTDIDF)), numOfk)
#        print listofCent
        for i in listofCent:
            k1.append(listTDIDF[i])    
            k.append(i)
            clusters.append(set({i}))
        print "Now Clustering First Sample"
        clusters = KMeans(k1,listTDIDF,clusters,k)
#        print clusters
        centList = updatedCentriods(clusters,listTDIDF)
        for i in range(0,10):
            print "Clustering Next Sample"
            clusters = KMeans1(centList,listTDIDF)
            centList = updatedCentriods(clusters,listTDIDF)
        
            
        SSE = calculateSSE(centList,clusters,listTDIDF)
#        return pd.DataFrame(clusters)
        print SSE
     except:
        print "Here"        
     
    

#if __name__ == "__main__":
#    main()
