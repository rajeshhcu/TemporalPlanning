 
#! /usr/bin/python

__author__="rajesh"
__date__ ="$May 30, 2009 8:09:45 AM$"

if __name__ == "__main__":
    print "Hello World";

import copy
#from extract import plan
#from extract import domainList
#from extract import beliefList
#from extract import planMetric
#from extract import target
from extract import *

global seedPlan
global domainList
global beliefs
global planMetric
global target


#def getActionBase():
 #   return actionBase
#def getBeliefBase():
    #return beliefList
#def getPlanList():
 #   return planList
#def getGoal():
 #   return goal
#def getGoalTime():
 #   return goal_time



#beliefList  = parseBeliefFile('beliefBase')
#planList = parsePlanFile('planLibrary')
#actionBase  = parseActionFile('actionBase')
#goal  = parseGoalFile('goal')
#goal_time = float(goal[len(goal)-1])

print " Enter the Seed plan path or  name"
#bFile = 'C:\\Python26\\TemporalPlanning1\\src\\test1.txt'
bFile = '/home/rajesht/Desktop/TemporalPlanning1/src/test1'
#bFile = 'beliefBase'
#bFile = raw_input()
seedPlan  = parsePlanFile(bFile)

print "Domain path or name "
#pFile = raw_input()
#pFile = 'C:\\Python26\\TemporalPlanning1\\src\\planproject\\domain.txt'
pFile = '/home/rajesht/Desktop/TemporalPlanning1/src/planproject/domain'
domainList = parseDomainFile(pFile)

print "BeliefList path or name "
#aFile = raw_input()
#aFile = 'C:\\Python26\\TemporalPlanning1\\src\\planproject\\init.txt'
aFile = '/home/rajesht/Desktop/TemporalPlanning1/src/planproject/init'
#aFile = 'actionBase'
beliefs = parseBeliefFile(aFile)

print "PlanMetric path or name "
#pmFile = 'C:\\Python26\\TemporalPlanning1\\src\\planproject\\planmetric.txt'
pmFile = '/home/rajesht/Desktop/TemporalPlanning1/src/planproject/planmetric'
planMetric = parsePlanMetricFile(pmFile)
#gFile = './rpg/goal'
#gFile = 'goal'
#goal  = parseGoalFile(gFile)
#goal_time = float(goal[len(goal)-1])

print "Target path or name"
#tFile = 'C:\\Python26\\TemporalPlanning1\\src\\planproject\\target.txt'
tFile = '/home/rajesht/Desktop/TemporalPlanning1/src/planproject/target'
target = parseTargetFile(tFile)

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


