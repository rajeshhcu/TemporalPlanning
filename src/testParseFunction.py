#! /usr/bin/python

__author__="rajender"
__date__ ="$May 19, 2009 7:17:46 AM$"

if __name__ == "__main__":
    print "Hello World";

from applicablePlans import getAllApplicablePlans
from relevantPlans import getRelevantPlan
from parseABGP import parseBeliefFile
from parseABGP import parsePlanFile
from parseABGP import parseGoalFile
from parseABGP import parseActionFile
from relevantPlans import unifyPlanLibraryAndGoal
from relevantPlans import *
from applicablePlans import applicablePlan_Main
from parseABGP import getBeliefList
from substituteGroundTerms import extendedPlans
from substituteGroundTerms import getExtendedPlans
#from RPG import relaxedPlanning_main

global goal_time

print "Belief Base "
beliefList  = parseBeliefFile('beliefBase')
print beliefList

print "Plan Library "
planList = parsePlanFile('planLibrary')
for i in range(len(planList)):
    print planList[i]

print "Action Base"
actionBase  = parseActionFile('actionBase')
for i in range(len(actionBase)):
    print actionBase[i]

print "Goal Element "
goal  = parseGoalFile('goal')
print goal

goal_time = float(goal[len(goal)-1])
print goal_time


test = unifyPlanLibraryAndGoal('planLibrary','goal')
print test
if (  test):
    print "No Plans matches with the Goal"
    #relaxedPlanning_main('actionBase','planLibrary','goal','beliefBase')

else:
    unifyPlanLibraryAndGoal('planLib','goal')
    relevantPlans = getRelevantPlan()
    print relevantPlans


    applicablePlan_Main(getRelevantPlan(),getBeliefList())
##
    applicablePlans = getAllApplicablePlans()
##
    extendedPlans(applicablePlans,actionBase)
#
    extendedApplicablePlans = (getExtendedPlans())
#
#    print len(extendedApplicablePlans)
#
    for i in range(len(extendedApplicablePlans)):
        print extendedApplicablePlans[i]

    #intension_main()
#    print relevantPlans
#    print applicablePlans
