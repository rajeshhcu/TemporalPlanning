import operator
import copy
#! /usr/bin/python

__author__="rajender"
__date__ ="$May 21, 2009 10:41:11 PM$"

if __name__ == "__main__":
    print "Heuristic Program ";


from testParseFunction import extendedApplicablePlans
from testParseFunction import  actionBase
from parseABGP import parseActionFile

def heuristic(eaPlans):
    print "heuristic Function"

    global plans_time
    plans_time = []
    plan_time = 0
    action = copy.deepcopy(parseActionFile('actionBase'))

    #print action_without_time
    #print action

    action_without_time = copy.deepcopy(actionBase)
    

    for i in range(len(eaPlans)):
        time =[]
        plan_time =0
        for j in range(len(eaPlans[i][2])):
            for k in range(len(action_without_time)):
                
                if(action_without_time[k]==eaPlans[i][2][j]):
                    plan_time += float(action[k][len(action[k])-1])

        time.append(i)
        time.append(plan_time)
        plans_time.append(time)
    #print "planIndex and PlanTime before sorting"
    #print plans_time
    plans_time = sorted(plans_time, key=operator.itemgetter(1))
    #print "After Sorting  on Plan Time "
    #print plans_time

def getSortedPlanIndex():
    print "getSortedPlanIndex Function "
    return plans_time

def allApplicableAfterPruning():
    print "allApplicableAfterPruning Function "
    return extendedApplicablePlans

def heuristic_main():
    print "Heuristic Main"
    temppEP  =  extendedApplicablePlans
    print temppEP
    print len(temppEP)
    #print "Heuristic Program "
    heuristic(temppEP)
heuristic_main()