#
#File: magic8Ball.py
#Compile: python3 magic8Ball.py
#
#


import random #used for random number generation


def getAnswer(answerNumber):
    """
    Function getAnswer()
    @params answerNumber
    Returns string value depending on guessed value
    """
    
    if answerNumber == 1:
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
        return 'My replay is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
    

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

