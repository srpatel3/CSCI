import random
import pandas as pd

def printstuff():
    print "Hello"

# takes two argument one is the dictionary and another is bag of words for doc
def computeTF(worDict, bow):
    tfDict = {}
    totalWordsInBag = len(bow)
    for word,count in worDict.iteritems():
        tfDict[word] = count/float(totalWordsInBag)
    return tfDict


# Should be able to calculate IDF

def computeIDF(dictList):
    import math
    idfDict = {}
    numOfDocs = len(dictList)
    # initize with words from first document
    idfDict = dict.fromkeys(dictList[0].keys(),0)
    for dictionary in dictList:
        for word, value in dictionary.iteritems():
            if value > 0:
                idfDict[word] += 1

    for word, value in idfDict.iteritems():
        idfDict[word] = math.log(numOfDocs / float(value))

    return idfDict

# Now would be the good time to Compute TFIDF
def computeTDIDF(tfBow,idfs):
    tfidf = {}
    for word, value in tfBow.iteritems():
        tfidf[word] = value * idfs[word]

    return tfidf


# Actually deals with clustering
def documentClustering(listBow):

    vocab = set()
    for bow in listBow:
        vocab = vocab.union(set(bow))

    listDict = []
    for i in range(0,len(listBow)):
        listDict.append(dict.fromkeys(vocab,0))

    for i in range(0,len(listBow)):
        for word in listBow[i]:
            listDict[i][word] += 1
#    return pd.DataFrame(listDict)
    return listDict
#    listtfBow = []
#    for i in range(0,len(listBow)):
#        listtfBow.append(computeTF(listDict[i],listBow[i]))
#    
#    idfs = computeIDF(listDict)
#
#    # Actually calculating TFIDF
#    listTFIDF = []
#    for i in range(0,len(listBow)):
#        listTFIDF.append(computeTDIDF(listtfBow[i],idfs))
##    return listTFIDF
##    print listTFIDF[0]
#    return listTFIDF









# Original Approach
# def documentClustering():
    # docA = "this cat sat on my face"
    # docB = "this god sat on my bed"
    # docC = "this cat sit on my bed"
    # bowA = docA.split(" ")
    # bowB = docB.split(" ")
    # bowC = docC.split(" ")
    # print bowA
    # print bowB
    # vocab = set()
    # for bow in listBow:
    #     vocab = vocab.union(set(bow))
    # print vocab
    # dictA = dict.fromkeys(vocab,0)
    # dictB = dict.fromkeys(vocab,0)
    # dictC = dict.fromkeys(vocab,0)
    # print dictA
    # for  bow in listBow:
    # for word in bowA:
    #     dictA[word] += 1
    #
    # for word in bowB:
    #     dictB[word] += 1
    # for word in bowC:
    #     dictC[word] += 1
    # print dictA
    # print dictB
    # Computing TF
    # print pd.DataFrame([dictA,dictB])
    # tfbowA = computeTF(dictA, bowA)
    # tfbowB = computeTF(dictB, bowB)
    # tfbowC = computeTF(dictC, bowC)
    # Computing IDF
    # print pd.DataFrame([tfbowA,tfbowB])
    # idfs = computeIDF(listDict)
    # Actually calculating TFIDF
    # tfidfBowA = computeTDIDF(tfbowA,idfs)
    # tfidfBowB = computeTDIDF(tfbowB, idfs)
    # tfidfBowC = computeTDIDF(tfbowC, idfs)
    # print pd.DataFrame(listTFIDF)
