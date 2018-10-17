# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 12:07:30 2018

@author: shiri
"""

import pandas as pd
import smtplib
from email.message import EmailMessage



def readData():
    print("Hello I am in readData function")
    pathName = "/home/sbot/CSCI191/CSCI191/Section1"
    fileName = "Section1ClassRolls.xlsx"
    fileLocation = pathName + "/" + fileName
    print(fileLocation)
    data = pd.ExcelFile(fileLocation)
#    spSheet = data.parse("crDetails")
    df1 = pd.read_excel(data, 'crDetails')
    names = df1.StudentName
    emails = df1.eMail
    Ids = df1.StudentID
    return names, emails, Ids


def sendEmail(nameList, emailList, idList):
    gmail_user = 'srpatel3@go.olemiss.edu'
    gmail_password = open("pass","r").readline()
    # print(gmail_password)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        for i in range(0,len(nameList)):
            # print("In here")
            sent_from = gmail_user
            to = emailList[i]
            # to = "shirish.patel218@gmail.com"
            # print("Here")
            subject = 'ALPHA TESTING'
            body = 'Hey, '+nameList[i]+'\n\t THIS IS TEST\n\n- Shirish Patel'
            # print("After body")
            email_text="From: "+sent_from+"\nTO: "+to+"\nSubject :"+subject+"\n"+body
            # print("Here????")
            # print("Text of the email:\n"+email_text+"\n\n")
            server.sendmail(sent_from,to,email_text)
            print("Email Sent to "+nameList[i]+"...!!!\n\n")
        server.close()

    except:
        print('Something went wrong...')


def main():
     nameList, emailList, idList = readData()
#
#     print(nameList)
#     print(emailList)
#     print(idList)
     sendEmail(nameList, emailList, idList)



main()
