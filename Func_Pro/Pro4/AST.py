from __future__ import annotations  # 3.7 deferred annotations
from typing import cast, Any, List, Mapping, Optional, Union
from dataclasses import dataclass  # 3.7
from abc import ABC, abstractmethod

# for varifying if Que is valid or not

# Class Text which only contains text
class Text:
	def __init__(self, text):
			self.text = text

	def getText(self):
		return self.text

# Class for a hintType

class HintType:
	def __init__(self, hintList):
		self.hintList = []
		for hint in hintList:
			self.hintList.append(Text(hint))
	def getHintType(self):
		contentToReturn = ""
		for hint in self.hintList:
			contentToReturn += hint.getText() + " "
		return contentToReturn
# Class for a single choice

class Choice:
	def __init__(self, choice):
		# print("Choice is : ",choice)
		# print("0")
		# print(choice[0])
		# print("1")
		# print(choice[1])
		# print("2")
		# print(choice[2])
		self.ans = Text(choice[1])
		if "Feedback" in choice[2]:
			temp = choice[2].split("Feedback")
			print(temp)
			print("Feedback found in choice")
			self.text = Text(temp[0])
			self.feedBack = Text(temp[1])
		else:
			self.text  = Text(choice[2])
			self.feedBack = Text('None')
		# self.feedBack = Text(feedBack)

	def getChoice(self):
		return self.text.getText() # + " "  + self.feedBack.getText()
# Class for only question
class Question:
	def __init__(self, question):
		# print(question)
		self.hintType = HintType(question[1])
		self.que = Text(question[2].replace('"',''))
		# print("hintType is : ",self.hintType)
		# print("Question is : ",self.text.getText())
	def getQuestion(self):
		# contentToReturn = ''
		return self.hintType.getHintType() + self.que.getText()+"\n"

# This would combine question with multiple choices
class QuestionBox:
	def __init__(self, questionBox):
		# print("0")
		# print(questionBox[0])
		# print("1")
		# print(questionBox[1])
		# print("2")
		# print(questionBox[2])
		self.question = Question(questionBox[0:3])

		self.choices = []
		for choice in questionBox[4]:
			self.choices.append(Choice(choice))
		# print(self.question)

	def getQuestionBox(self):
		contentToReturn = ""
		contentToReturn += self.question.getQuestion()
		for choice in self.choices:
			contentToReturn += "\t" + choice.getChoice() + "\n"
		contentToReturn += '\n\n\n'
		return contentToReturn

class Exam:
	def __init__(self,title, queBoxes):
		self.title = title[0][1]
		self.queBoxes = []
		for queBox in queBoxes:
			self.queBoxes.append(QuestionBox(queBox))
		# Parsing choicebox logic should go here
	def getExam(self):
		return self.getComponents()

	def getComponents(self):
		contentToReturn = self.title + "\n"
		for queBox in self.queBoxes:
			contentToReturn += queBox.getQuestionBox()
		return contentToReturn
# def main():
# 	print("Hello World")
#
# if __name__ == "__main__":
# 	main()
