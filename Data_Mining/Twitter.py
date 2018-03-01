import tweepy
from tweepy import OAuthHandler
import json
import datetime as dt
import time
import os
import sys
import csv
import re
from collections import Counter

#This function creates and returns an API Object
def get_API_Object():
    customer_Key = 'XAuGWImYBJbu0JtsJfstoDQ6f'
    customer_Secret = 'Apu58Bx1FcyrXh76qcEZKDVHflPblVBpUeLPVvpL31JpqeWl7k'
    access_Secret = 'xgIL9fdsHj9nZoFthDljkn4vaoyOO2U6RobmIuJ2QYPqa'
    access_Token = '2700821466-whqq238Y02NDhHlxftHOdhqUIocskUhm8kQKGok'

    temp = OAuthHandler(customer_Key, customer_Secret)
    temp.set_access_token(access_Token, access_Secret)

    return tweepy.API(temp)


#This function gets ID's of tweets to retriew

def get_tweet_id(API_Object, date = '', days_ago=7,query = "#healthy"):

    if date:
        # return an ID from the start of the given day
        td = date + dt.timedelta(days=1)
        tweet_date = '{0}-{1:0>2}-{2:0>2}'.format(td.year, td.month, td.day)
        tweet = API_Object.search(q=query, count=1, until=tweet_date)
    else:
        # return an ID from __ days ago
        td = dt.datetime.now() - dt.timedelta(days=days_ago)
        tweet_date = '{0}-{1:0>2}-{2:0>2}'.format(td.year, td.month, td.day)
        # get list of up to 10 tweets
        tweet = API_Object.search(q=query, count=10, until=tweet_date)
        #print('search limit (start/stop):',tweet[0].created_at)

        print 'tweet is:',tweet[5].text
        for i in range(0,10):
            print '[',i,']',tweet[i].hashtags
        # return the id of the first tweet in the list
        return tweet[0].id



def main():
    hashtag = "#healthy"
    min_days_old = 1
    max_days_old = 7
    API_Object = get_API_Object()
    # csvFile = open('ua.csv', 'a')
    # #Use csv Writer
    # csvWriter = csv.writer(csvFile)
    # #Now getting tweet ID
    # #max_id = get_tweet_id(API_Object, days_ago=(min_days_old-1))
    # #since_id = get_tweet_id(API_Object, days_ago=(max_days_old-1))
    # #print "max is is", max_id, "and Min ID is : "
    # print "loading"
    # count = 0
    # for tweet in tweepy.Cursor(API_Object.search,q="#healthy",
    #                        lang="en",
    #                        since="2018-02-22").items():
    #     #print (tweet.created_at, tweet.text)
    #     print count
    #     count = count+1
    #     if count > 700:
    #         print "Sleeping"
    #         time.sleep(20)
    #         count = 0
    #     csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

    # Let's start processing this shit
    list_hashtags = []
    with open('ua.csv','rb') as csvfile:
        #line = csv.reader(csvfile, delimiter=',')
        #for line in csvfile:
        for i in range(0,10):
            line = csvfile.readline()
            line = line.lower()
            hashtags = re.findall(r"#(\w+)",line)
            for tags in hashtags:
                # print tags
                # if tags not in list_hashtags:
                list_hashtags.append(tags)



        items = dict(Counter(list_hashtags))
        #sorted(student_tuples, key=lambda student: student[2])

        dictlist = []
        for key, value in items.iteritems():
            temp = [key,value]
            dictlist.append(temp)
        dictlist1 = sorted(dictlist, key=lambda tag: tag[1],reverse = True)
        print dictlist1


if __name__ == "__main__":
    main()
