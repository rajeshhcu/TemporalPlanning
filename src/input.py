#! /usr/bin/python

__author__="rajender"
__date__ ="$May 30, 2009 8:09:45 AM$"

if __name__ == "__main__":
    print "Hello World";

from parseABGP import parseBeliefFile
from parseABGP import parsePlanFile
from parseABGP import parseGoalFile
from parseABGP import parseActionFile

global goal_time
global goal
global beliefList
global planList
global actionBase


def getActionBase():
    return actionBase
def getBeliefBase():
    return beliefList
def getPlanList():
    return planList
def getGoal():
    return goal
def getGoalTime():
    return goal_time



#beliefList  = parseBeliefFile('beliefBase')
#planList = parsePlanFile('planLibrary')
#actionBase  = parseActionFile('actionBase')
#goal  = parseGoalFile('goal')
#goal_time = float(goal[len(goal)-1])

print " Enter the BeliefBase path or  name"
bFile = './rpg/beliefBase'
#bFile = 'beliefBase'
#bFile = raw_input()
beliefList  = parseBeliefFile(bFile)

print "PlanBase path or name "
#pFile = raw_input()
pFile = 'planLib'
planList = parsePlanFile(pFile)

print "ActionBase path or name "
#aFile = raw_input()
aFile = './rpg/actionBase'
#aFile = 'actionBase'
actionBase  = parseActionFile(aFile)

print "Goal path or name "
#gFile = raw_input()
gFile = './rpg/goal'
#gFile = 'goal'
goal  = parseGoalFile(gFile)
goal_time = float(goal[len(goal)-1])

#del aFile,bFile,pFile,gFile

#print getBeliefBase()
#print getActionBase()
#print getPlanList()
#print getGoal()
#print getGoalTime()

#print "Belief Base "
#
#print getBeliefBase()
#
#print "Plan Library "
#
#for i in range(len(getPlanList())):
#    print getPlanList()[i]
#
#print "Action Base"
#
#for i in range(len(getActionBase())):
#    print getActionBase()[i]
#
#print "Goal Element "
#
#print goal
#
#goal_time = float(goal[len(goal)-1])
#print goal_time


