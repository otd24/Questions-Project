#File name: questions.py
#Author: Olivia Do
#Purpose: This program is a simple quiz system
#Date: 23 October 2024

from abc import ABC, abstractmethod

class Question(ABC): 
    def __init__(self, prompt, correctAnswer = '', points = 0):
        self.__prompt = prompt
        self.__correctAnswer = correctAnswer
        self.__points = points
        
    # overload the str method
    def __str__(self):
        promptStr = f'Prompt: {self.getPrompt()}\n'
        correctAnswerStr = f'Correct Answer: {self.getCorrectAnswer()}\n'
        pointsStr = f'Points: {self.getPoints}'
        finalStr = promptStr + correctAnswerStr + pointsStr
        return finalStr
    
    @abstractmethod
    def displayForTest(self):
        pass
        #testString = ''
        #testString += f'Prompt: {self.getPrompt()}\n'
        #testString += f'Correct Answer: {self.getCorrectAnswer()}\n'
        #testString += f'Points: {self.getPoints()}'
        #return testString
        
        
    # getters
    def getPrompt(self):
        return self.__prompt
    
    def getCorrectAnswer(self):
        return self.__correctAnswer
    
    def getPoints(self):
        return self.__points
    
    # setters
    def setPrompt(self, prompt):
        self.__prompt = prompt
    
    def setPoints(self, points):
        self.__points = points
        
    def setCorrectAnswer(self, correctAnswer):
        self.__correctAnswer = correctAnswer
    
    # multiple choice derived class

class MultipleChoice(Question):
    def __init__(self, prompt, choices = [], correctAnswer = '', points = 0):
        super().__init__(prompt, correctAnswer, points) 
        self.__choices = choices
        
    # getters
    def getChoices(self):
        return self.__choices
        
    # setters
    def addChoice(self, choiceToAdd):
        self.__choices.append(choiceToAdd)
        
    def updateChoice(self, index, wording):
        self.__choices[index] = wording
        
    # displayForTest method
    def displayForTest(self):
        testString = ''
        testString += self.getPrompt()
        for i in range(len(self.getChoices())):
            testString += '\n' + self.getChoices()[i]
        testString += '\n'
        return testString
    
    def __str__(self):
        promptStr = f'Prompt: {self.getPrompt()}\n'
        correctAnswerStr = f'Correct Answer: {self.getCorrectAnswer()}\n'
        pointsStr = f'Points: {self.getPoints()}\n'
        choices = f'Choices: {self.getChoices()}'
        finalStr = promptStr + correctAnswerStr + pointsStr + choices
        return finalStr

class ShortAnswer(Question):
    def __init__(self, prompt, length, correctAnswer = '', points = 0):
        super().__init__(prompt, correctAnswer, points)
        self.__length = length
    
    # getters
    def getLength(self):
        return self.__length
    
    # setters 
    def setLength(self, length):
        self.__length = length
    
    # displayForTest
    def displayForTest(self):
        testString = f'{self.getPrompt()} (up to {self.getLength()} characters)'
        return testString
        
    # override str method from parent class
    def __str__(self):
        promptStr = f'Prompt: {self.getPrompt()}\n'
        correctAnswerStr = f'Correct Answer: {self.getCorrectAnswer()}\n'
        pointsStr = f'Points: {self.getPoints()}\n'
        lengthStr = f'Character limit: {self.getLength()}'
        finalStr = promptStr + correctAnswerStr + pointsStr + lengthStr
        return finalStr
    
class FillInTheBlank(Question):
    def __init__(self, prompt, correctAnswer = '', points = 0):
        super().__init__(prompt, correctAnswer, points)
    
    # display for test
    def displayForTest(self):
        testString = f'Fill in the blank:\n{self.getPrompt()}'
        return testString

        
        
    # str implementation
    def __str__(self):
        testStr = f'Prompt: {self.getPrompt()}\n'
        testStr += f'Correct Answer: {self.getCorrectAnswer()}\n'
        testStr += f'Points: {self.getPoints()}\n'
        return testStr
    
    
        
        
    
        
        
        
    

    
    
        
        