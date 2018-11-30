from parsita import TextParsers, opt, rep, reg



class TreeParsers(TextParsers): 
    # Grammar rules using Parsita, with semantic routines
    exam = opt(title) & questionBox # > make_binop 
    questionBox = rep(question)
    question = reg(r"Question ") & opt(listt) & text & opt(hint) & choiceBox
    choiceBox =  rep(choiceCorrect | choice)
    choice = reg(r"Choice ") & opt(reg(r"\s*")) & text & reg(r"\s*") & opt(feedback)
    choiceCorrect = reg(r"Choice ") & opt(reg(r"\s*correct\s*")) & text & reg(r"\s*") & opt(feedback)
    feedback = reg(r"Feedback ")
    listt = reg(r"\[\".+\"(?:,.+)?\]")
    hint = reg(r"Hint ") & text
    title = reg(r"^Exam ") & text
    text = reg(r"\".+\"(?:\n,\n)?")

#temp = "Question [\"curriculum\", \"course\"] \"Which of the following is a required course?\"\nHint \"It is a 400-level course.\"\nChoice         \"CSci 323\" Feedback \"Systems Programming is elective.\"\nChoice correct \"CSci 450\" Feedback \"Programming Languages is core.\"\nChoice         \"CSci 525\" Feedback \"Compiler Construction is elective.\"\n"
#temp = "Choice         \"CSci 323\" Feedback \"Systems Programming is elective.\"\nChoice correct \"CSci 450\" Feedback \"Programming Languages is core.\"\nChoice         \"CSci 525\" Feedback \"Compiler Construction is elective.\"\n"
#temp = "Exam \"Curriculum Test\"\nQuestion [\"curriculum\", \"course\"] \"Which of the following is a required course?\"\nHint \"It is a 400-level course.\"\nChoice         \"CSci 323\" Feedback \"Systems Programming is elective.\"\nChoice correct \"CSci 450\" Feedback \"Programming Languages is core.\"\nChoice         \"CSci 525\" Feedback \"Compiler Construction is elective.\"\nQuestion [\"language\",\"course\"]\n    \"What one of the following languages is used in CSci 556?\"\nChoice         \"Lua\" \nChoice         \"Elixir\"\nChoice         \"Scala\"\nChoice         \"Haskell\"\nChoice correct \"Python 3\"\nChoice         \"Rust\"\n\nQuestion \"Are ready for Thanksgiving Break?\"\nHint \"Is this a valid question?\"\nChoice correct \"Yes\"\nChoice correct \"No\"\nChoice         \"Maybe\"\n"
temp = "Exam \"Curriculum Test\"\nQuestion [\"curriculum\", \"course\"] \"Which of the following is a required course?\"\n    Hint \"It is a 400-level course.\"\nChoice         \"CSci 323\" Feedback \"Systems Programming is elective.\"\nChoice correct \"CSci 450\" Feedback \"Programming Languages is core.\"\nChoice         \"CSci 525\" Feedback \"Compiler Construction is elective.\"\nQuestion [\"language\",\"course\"]\n    \"What one of the following languages is used in CSci 556?\"\nChoice         \"Lua\" \nChoice         \"Elixir\"\nChoice         \"Scala\"\nChoice         \"Haskell\"\nChoice correct \"Python 3\"\nChoice         \"Rust\"\n\nQuestion \"Are ready for Thanksgiving Break?\"\nHint \"Is this a valid question?\"\nChoice correct \"Yes\"\nChoice correct \"No\"\nChoice         \"Maybe\"\n"
tree = TreeParsers().exam.parse(temp)
print('Tree:', tree)


#class TreeParsers(TextParsers): 
#    # Grammar rules using Parsita, with semantic routines
##    exam = opt(title) & rep(questionBox) # > make_binop 
##    questionBox = question & opt(hint) & choiceBox 
##    question = reg(r"Question(\s)*") & opt(hintType) & text
##    hintType = reg(r"\[((\"|\')[a-zA-Z0-9]*((\"|\')(\s)*\,(\s)*)?)*(\"|\')[a-zA-Z0-9]*(\"|\')\]")
##    choiceBox =  rep(choiceCorrect | choice)
##    choice = reg(r"Choice(\s)*") & (feedback|text)
##    choiceCorrect = reg(r"Choice correct(\s)*") & (feedback|text)
##    feedback = reg(r"Feedback(\s)*") & text
##    hint = reg(r"Hint(\s)*") & text
##    title = reg(r"Exam(\s)*") & text
#    text = reg(r"^.{2,}$\n")
#
##temp = "Exam \"Curriculum Test\"\nQuestion [\"curriculum\", \"course\"] \"Which of the following is a required course?\"\n    Hint \"It is a 400-level course.\"\nChoice         \"CSci 323\" Feedback \"Systems Programming is elective.\"\nChoice correct \"CSci 450\" Feedback \"Programming Languages is core.\"\nChoice         \"CSci 525\" Feedback \"Compiler Construction is elective.\"\nQuestion [\"language\",\"course\"]\n    \"What one of the following languages is used in CSci 556?\"\nChoice         \"Lua\" \nChoice         \"Elixir\"\nChoice         \"Scala\"\nChoice         \"Haskell\"\nChoice correct \"Python 3\"\nChoice         \"Rust\"\n\nQuestion \"Are ready for Thanksgiving Break?\"\nHint \"Is this a valid question?\"\nChoice correct \"Yes\"\nChoice correct \"No\"\nChoice         \"Maybe\"\n"
#temp = "\"Curriculum Test\"\n"
##temp = "Exam \"Curriculum Test\"\n\nQuestion [\"curriculum\", \"course\"] \"Which of the following is a required course?\"\nHint \"It is a 400-level course.\"\nChoice         'CSci 323' Feedback 'Systems Programming is elective.'\nChoice correct 'CSci 450' Feedback 'Programming Languages is core.'\nChoice         'CSci 525' Feedback 'Compiler Construction is elective.'\nQuestion [\"curriculum\", \"course\"] \"Which of the following is a required course?\"\nHint \"It is a 400-level course.\"\nChoice         'CSci 323' Feedback 'Systems Programming is elective.'\nChoice correct 'CSci 450' Feedback 'Programming Languages is core.'\nChoice         'CSci 525' Feedback 'Compiler Construction is elective.'\nQuestion [\"curriculum\", \"course\"] \"Which of the following is a required course?\"\nHint \"It is a 400-level course.\"\nChoice         'CSci 323' Feedback 'Systems Programming is elective.'\nChoice correct 'CSci 450' Feedback 'Programming Languages is core.'\nChoice         'CSci 525' Feedback 'Compiler Construction is elective.'\n"
#tree = TreeParsers().text.parse(temp)
#print('Tree:', tree)