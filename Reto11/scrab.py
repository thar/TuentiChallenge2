#!/usr/bin/python

#########################################################################
# Program will create words for scrabble given letters and words already
# Date Created: 6/15/11
# Date Finished: TBA
# FileName: Scrabble.py
#########################################################################

#Modificado por: Miguel Angel Julian Aguilar
#Ajustado para el Tuenti contest
#e-mail: miguel.a.j82@gmail.com


import itertools
from sets import Set
import sys


getPoints={}
getPoints['a']=1
getPoints['e']=1
getPoints['i']=1
getPoints['l']=1
getPoints['n']=1
getPoints['o']=1
getPoints['r']=1
getPoints['s']=1
getPoints['t']=1
getPoints['u']=1
getPoints['d']=2
getPoints['g']=2
getPoints['b']=3
getPoints['c']=3
getPoints['m']=3
getPoints['p']=3
getPoints['f']=4
getPoints['h']=4
getPoints['v']=4
getPoints['w']=4
getPoints['y']=4
getPoints['k']=5
getPoints['j']=8
getPoints['x']=8
getPoints['q']=10
getPoints['z']=10

def getWordPoints(word):
    global getPoints
    points=0
    for letter in word:
        points=points+getPoints[letter.lower()]
    return points

#########################################################################
# Class implements program mechanics
# Such as setting up global variables and...
# Handling events and procedures used in the program
#########################################################################
class Program:
        # CTOR and Set up values
        def __init__(self):
                self.words = []
                self.letters = []
                # Load words in dictionary file
                self.maxLength=0
                self.dictionaryEntries = Set(x.strip() for x in open('descrambler_wordlist.txt', 'r').readlines())
                for w in self.dictionaryEntries: self.maxLength=max(self.maxLength, len(w))




        #####################################################################
        # FindWords - Find Words give letters user has and...
        # Words on the board
        # Returns a list of possible words
        #####################################################################
        def FindWords(self, words, letters):
                self.words = words
                self.letters = letters
                possibleResults = [('',0)]
                possibleWords = ['']
                letterCombinations = self.Rotate()
                combo = ''

                # Check if possible to add on word on to existing word
                for x in letterCombinations:
                        # Convert tuple of letters to one continuous string
                        combo = ''.join(x)
                        for word in self.words:
                                # Check if combination can be added on, before...
                                # Or inbetween
                                for i in range(len(combo) + 1):
                                        #if combo[:len(combo) - i] + word + combo[len(combo) - i:] in self.dictionaryEntries:
                                        #        possibleWords.append(combo[:len(combo) - i] + word + combo[len(combo) - i:])

                                        for letter in word:
                                                newWord=combo[:len(combo) - i] + letter + combo[len(combo) - i:]
                                                if newWord in self.dictionaryEntries and newWord not in possibleWords:
                                                        wordPoints=getWordPoints(newWord)
                                                        if wordPoints>possibleResults[0][1]:
                                                            possibleResults=[(newWord,wordPoints)]
                                                            possibleWords=[newWord]
                                                        elif wordPoints==possibleResults[0][1]:
                                                            possibleResults.append((newWord,wordPoints))
                                                            possibleWords.append(newWord)


                        combo = ''

                return possibleResults



        #####################################################################
        # Rotate - Find different combinations of letters passed in as...
        # Member of class
        # Returns a list of the letter combinations
        #####################################################################
        def Rotate(self):
                # Contains letter combinations
                x = []

                # Find all possible letter combinations
                for i in range(1, len(self.letters) + 1):
                        for j in itertools.permutations(self.letters, min(i,self.maxLength)):
                                x.append(j)

                return x



lines=sys.stdin.readlines()
nCases=int(lines.pop(0).strip())
program = Program()

for line in lines:
    lineData=line.strip().split()
    myletters=list(lineData[0].upper())
    deskWords=[lineData[1].upper()]


    res=program.FindWords(deskWords, myletters)
    res=sorted(res, key=lambda word: (word[0],word[1]))
    print '%s %d' % res[0]


