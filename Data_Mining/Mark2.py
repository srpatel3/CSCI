import pandas as pd
import pprint
fileToOpen = "/home/shirish/Data_Files/twitter_csci581_revised.csv"



try:
	pp = pprint.PrettyPrinter(indent=4)
	Data = open(fileToOpen,"r")
	for i in range(0,100):
		line = Data.readline()
		pp.pprint(line)



	# This will be used to Read data later on
	# Data = open(fileToOpen,"r")
	# for chunck_df in pd.read_csv(fileToOpen, chunksize=100):
	# 	print "File Successfully Opened"
	# 	pp.pprint(chunck_df)
	# 	break
	# 	# count = 0
		# while count <10:
		# pp.PrettyPrinter(chunck_df)
		# line  = chunck_df.readline()
		# print line
		# count += 1

except:
	print "Error Opening File"

try:
	Data.close()
	print "And File Suceessfully Closed"
except:
	print "Error while closing file"
