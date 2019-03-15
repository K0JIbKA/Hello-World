import random                           # imports the 'random' module
def getAnswer(answerNumber):            # the 'getAnswer()' function is defined
    if answerNumber == 1:               # the program execution moves to the top of the 'getAnswer()' function
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
r = random.randint(1, 9)                # the 'random.randint(1, 9)' function is called with 2 random arguments between 1 and 9
fortune = getAnswer(r)                  # 'getAnswer()' function is called with 'r' as argument
print(fortune)                          # the returned string is assigned to a variable named 'fortune' which gets passed to a 'print()' call
