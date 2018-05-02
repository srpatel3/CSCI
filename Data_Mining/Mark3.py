import os
import string
import operator
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

def main():
    # print "Hii inside main"
    path = "/home/shirish/Data_Files/Machine_Learning/20news-18828/"
    dirs = os.walk(path)
    count = 0
    directory_Dicts = []
    dirList = []
    for roots,dirs,files in os.walk(path):
        directory = dirs
        for dirs in directory:
            temp = {}
            dirList.append(dirs)
            for files in os.walk(path+"/"+dirs):
                fileList = files[2]
                for files in fileList:
                    readFile = open(path+"/"+dirs+"/"+files,"r")
                    getDict(readFile,temp)
            directory_Dicts.append(temp)
        break
    dir_Dict = {}
    for i in range(0,len(dirList)):
        dir_Dict[dirList[i]] = len(directory_Dicts[i])
    dir_Dict = list(sorted(dir_Dict.items(), key=lambda x:x[1], reverse=True))
    for item in dir_Dict:
        print item

    directory_Dicts.sort(reverse=True,key= len)

    # for i in range(0,5):
        # print len(directory_Dicts[i])
        # print directory_Dicts[i]

    for item in directory_Dicts:
        print len(item)
    # print len(directory_Dicts[0])

if __name__ == "__main__":
    main()
