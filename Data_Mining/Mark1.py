import random

fileToRead = open("twitter_csci581.csv","r")
print "Reading File"
inputData = fileToRead.readlines()
fileToRead.close()
print "Shuffling Data"
random.shuffle(inputData)
print "Shuffling Done."
fileToWrite = open("twitter_csci581_revised.csv","w")

print "Now Writing Data to file"
fileToWrite.writelines(inputData)
print "Writing Done."
fileToWrite.close()
