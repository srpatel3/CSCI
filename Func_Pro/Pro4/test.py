# To do List
# Question Validation : Return true or false
# Hint validation : Return True or false
# Choice validation : Return True or false

from parsita import TextParsers, opt, rep, reg
from AST import Exam

def formatString(parse_res):
	# print("Length of parse Res is :"+str(len(parse_res)))
	# print(parse_res[0])
	# print('Length of second List is:'+str(len(parse_res[1])))
	# tempList = parse_res[1]
	# print("0")
	# print(tempList[0])
	# print("1")
	# print(tempList[1])
	# print("2")
	# print(tempList[2])
	exam = Exam(parse_res[0],parse_res[1]).getExam()
	print(exam)
	# print(parse_res[1])
	return "Blah Blah"


class TreeParsers(TextParsers):
	exam = opt(title) & questions  > formatString
	questions = rep(actualQuestion)
	actualQuestion = reg(r"Question ") & opt(listt) & text & opt(hint) & mulChoices
	mulChoices =  rep(choiceCorrect | singleChoice)
	singleChoice = reg(r"Choice ") & opt(reg(r"\s*")) & text & reg(r"\s*") & opt(feedback)
	choiceCorrect = reg(r"Choice ") & opt(reg(r"\s*correct\s*")) & text & reg(r"\s*") & opt(feedback)
	feedback = reg(r"Feedback ")
	listt = reg(r"\[\".+\"(?:,.+)?\]")
	hint = reg(r"Hint ") & text
	title = reg(r"^Exam ") & text
	text = reg(r"\".+\"(?:\n,\n)?")


input = "Exam \"Curriculum Test\"\nQuestion [\"curriculum\", \"course\"] \"Which of the following is a required course?\"\n    Hint \"It is a 400-level course.\"\nChoice         \"CSci 323\" Feedback \"Systems Programming is elective.\"\nChoice correct \"CSci 450\" Feedback \"Programming Languages is core.\"\nChoice         \"CSci 525\" Feedback \"Compiler Construction is elective.\"\nQuestion [\"language\",\"course\"]\n    \"What one of the following languages is used in CSci 556?\"\nChoice         \"Lua\" \nChoice         \"Elixir\"\nChoice         \"Scala\"\nChoice         \"Haskell\"\nChoice correct \"Python 3\"\nChoice         \"Rust\"\n\nQuestion \"Are ready for Thanksgiving Break?\"\nHint \"Is this a valid question?\"\nChoice correct \"Yes\"\nChoice correct \"No\"\nChoice         \"Maybe\"\n"
output = TreeParsers().exam.parse(input)
