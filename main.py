#File name: main.py
#Author: Olivia Do
#Purpose: This program is a simple quiz system
#Date: 23 October 2024

from questions import *

def answerQuestion(question):
    print(question.displayForTest())
    userAnswer = input('Enter your answer: ')
    print()
    return userAnswer

def gradeQuestion(question, userAnswer):
    if userAnswer.lower() == question.getCorrectAnswer().lower():
        return question.getPoints()
    elif userAnswer.lower() != question.getCorrectAnswer().lower():
        return 0
    
    


if __name__ == "__main__" :
    mcQuestion = MultipleChoice('What color is the sky?', ['a.red', 'b.blue', 'c.green'], 'b', 3)
    mcQuestion2 = MultipleChoice('What do rabbits eat?', ['a.carrots', 'b.coffee', 'c.dragons'], 'a', 3)
    shortAnswer = ShortAnswer('What is potassium on the periodic table?', 1, 'K', 3)
    shortAnswer2 = ShortAnswer('What is the meaning of life?', '11', 'To be happy', 3)
    Blank = FillInTheBlank('The United States has __ states', 'fifty', 3)
    Blank2 = FillInTheBlank('Pineapple on pizza is so ____', 'good!', 3)
    listQuestions = [mcQuestion, mcQuestion2, shortAnswer, shortAnswer2, Blank, Blank2]
    points = 0
    for i in range(len(listQuestions)):
        points += gradeQuestion(listQuestions[i], answerQuestion(listQuestions[i]))
    print(f'You earned: {points} points')
    
    
    
    