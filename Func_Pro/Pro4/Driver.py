from parsita import TextParsers, opt, rep, reg 

class TreeParsers(TextParsers):
	# Grammar rules using Parsita, with semantic routines
	exam = opt(title) & rep(questionBox) # > make_binop
	questionBox = question & opt(hint) & choiceBox
	question = reg(r"Question(\s)*") & opt(hintType) & text
	hintType = reg(r"\[((\"|\')[a-zA-Z0-9]*((\"|\')(\s)*\,(\s)*)?)*(\"|\')[a-zA-Z0-9]*(\"|\')\]")
	choiceBox = repsep(choice | choiceCorrect)
	# choiceBox = choice
	choice = reg(r"Choice[\s]+") & text
	choiceCorrect = reg(r"Choice correct(\s)*") & text
	hint = reg(r"Hint[\s]+") & text
	title = reg(r"Exam[\s]+") & text
	text = reg(r"[\w\W]*\n")
    
tree = TreeParsers().title.parse('Exam "Curriculum Test"\n')
print('Tree:', tree)
# hint = TreeParsers().hint.parse('Hint "Hint Test"\n')
# print("Hint:", hint)
# choice = TreeParsers().choice.parse('Choice "Choice"\n')
# print('Choice:',choice)
# choice_c = TreeParsers().choiceCorrect.parse('Choice correct "Choice Correct"\n')
# print('Choice Correct:',choice_c)
choice_box = TreeParsers().choiceBox.parse('Choice correct "Choice Correct"\Choice "Choice Something1"\n')
print('Choice Box:',choice_box)
# hintType = TreeParsers().hintType.parse("[\"curriculum\", \"course\"]")
# print('HintType:',hintType)
# que = TreeParsers().question.parse('Question ["curriculum", "course"] "Which of the following is a required course?"\n')
# print('Question:', que)
# queBox = TreeParsers().questionBox.parse('Question ["curriculum", "course"] "Which of the following is a required course?"\nHint "It is a 400-level course."\nChoice         "CSci 323"\nChoice         "CSci 525"\n')
# print('QuestionBox',queBox)
# exam = TreeParsers().exam.parse('Exam "Curriculum Test"\nQuestion ["curriculum", "course"] "Which of the following is a required course?"\nHint "It is a 400-level course."\nChoice         "CSci 323"\nChoice correct "CSci 450"\nChoice         "CSci 525"\nQuestion ["language","course"] "What one of the following languages is used in CSci 556?"\nChoice         "Lua"\nChoice         "Elixir"\nChoice         "Scala"\nChoice         "Haskell"\nChoice correct "Python 3"\nChoice         "Rust"\nQuestion "Are ready for Thanksgiving Break?"\nHint "Is this a valid questions?"\nChoice correct "Yes"\nChoice correct "No"\nChoice         "Maybe"')
# exam = TreeParsers().exam.parse('Exam "Curriculum Test"\nQuestion ["curriculum", "course"] "Which of the following is a required course?"\nHint "It is a 400-level course."\nChoice         "CSci 323"\nChoice correct "CSci 450"\nChoice         "CSci 525"\nQuestion ["language","course"] "What one of the following languages is used in CSci 556?"\nChoice         "Lua"\nChoice         "Elixir"\nChoice         "Scala"\nChoice         "Haskell"\nChoice correct "Python 3"\nChoice         "Rust"\n')
# print('Exam:',exam)


