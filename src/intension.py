#from testParseFunction import goal_time
from input import getGoal
from input import goal_time
from input import bFile
from input import gFile
from input import aFile
from input import pFile
from testParseFunction import beliefList
from heuristic import allApplicableAfterPruning
from heuristic import getSortedPlanIndex
#from substituteGroundTerms import removeDuplicatePlans

import copy
#! /usr/bin/python

__author__="rajender"
__date__ ="$May 22, 2009 12:20:52 PM$"

if __name__ == "__main__":
    print "Intension";

from parseABGP import getActionList
from heuristic import heuristic_main
from input import *
from RPG import relaxedPlanning_main

def selectIndex(bList,se):
    print "selectIndex Function "

    tse = copy.deepcopy(se)
    print tse
    for i in range(len(bList)):
        print "BL ",bList[i]

        if(tse == bList[i]):
            print i
            return int(i)


def addEffectsIntoStack(stack,se,bl):
    print "addEffectsIntoStack Function "
    a_plan = getActionPlans()
    for i in range(len(a_plan)):
        if(se == a_plan[i][0]):
            break
    if(selectValidPlan(bl,a_plan[i])):
        for j in range(len(a_plan[i][2])):
            stack.append(a_plan[i][2][j])
    else:
        return False

    return True

def selectValidPlan(bl,a_plan):
    print "selectValidPlan Function "

    for i in range(len(a_plan[1])):

        value = False
        for j in range(len(bl)):
            if(a_plan[1][i]==bl[j]):
                value  = True
                break
        if(value):
            continue
        else:
            return False
    return True

def intension(stack,bl,goal):
    print "intension Function "

    cond =True
    print "********************************************************************"
    while cond:
        if(stack != []):
            stackelement = stack.pop()
            print "stackelement ",stackelement
        else:
            break

        if(stackelement==[]):
            v = False
        else:
            if(stackelement[0]=='+'):
                del stackelement[0]
                bl.append(stackelement)
                print bl
                v =True
            elif(stackelement[0] == '-'):
                del stackelement[0]
                print "Stack Element after deletion of First ",stackelement
                index = selectIndex(bl,stackelement)
                print index
                del bl[index]
                print bl
                v = True
            elif(stackelement[0]=='!'):
            #plan = getPlan(stackelement)
            #goal = stackelement
            #plan = getPlan(goal)

                print "I need to implement for this "
            else:

                v = addEffectsIntoStack(stack,stackelement,bl)
                print "V : " ,v
        print " STACK : " , stack
        if(v):
            cond = True
        else:
            cond = False
    print "********************************************************************"
    
    print "********************************************************************"
    if(stack == []):
        return True
    else:
        return False
#    stackelement = stack.pop()
#    print "stackelement ",stackelement
#
#    if(stackelement==[]):
#        return True
#    else:
#        if(stackelement[0]=='+'):
#            bl.append(stackelement)
#            v =True
#        elif(stackelement[0] == '-'):
#            index = selectIndex(bl,stackelement)
#            del bl[index]
#            v = True
#        elif(stackelement[0]=='!'):
#            #plan = getPlan(stackelement)
#            #goal = stackelement
#            #plan = getPlan(goal)
#
#            print "I need to implement for this "
#        else:
#
#           v = addEffectsIntoStack(stack,stackelement,bl)
#    if(v):
#        return True
#    else:
#        return False

def unifyPossibleActions(a):
#    print "Unify Actions with plans "
    
    unifyPlanList =[]
    for i in range(len(planBase)):
        if((len(a)-1)==len(planBase[i][0])):
            #print a , planBase
            if(a[0]==planBase[i][0][0]):
                unifyPlanList.append(planBase[i])

    return unifyPlanList[0]

def applyGTtoPlan(a,p):
    #print " applyGTtoPlan_RPG Function "
    l =[]
    list =[]
    condition=False
    tempPlan = copy.deepcopy(p)

    #print a
    #print tempPlan , len(tempPlan)

    for i in range(len(tempPlan)):

        if(a[0]==tempPlan[i][0][0]):
#            print tempPlan[i][0][0]
            for j in range(len(a)-1):
#                print a[j]
                if(a[j] ==tempPlan[i][0][j]):
#                    print tempPlan[i][0][j]
                    continue
                elif(tempPlan[i][0][j].isupper()):
                    l.append(tempPlan[i][0][j])
                    l.append(a[j])
                    list.append(l)
                    l =[]
                    condition = True
                else:
                    continue
            if(condition):
                break
    v = copy.deepcopy(i)
    planN = tempPlan[i][0]
    planP = tempPlan[i][1]
    planE = tempPlan[i][2]

    for i in range(len(planN)):
        if(planN[i].isupper()):
            value = getValue_RPG(planN[i],list)
            planN[i] = value

    for i in range(len(planP)):
        for j in range(len(planP[i])):

            if(planP[i][j].isupper()):
                value = getValue_RPG(planP[i][j],list)
                planP[i][j] = value
    for i in range(len(planE)):
        for j in range(len(planE[i])):

            if(planE[i][j].isupper()):
                value = getValue_RPG(planE[i][j],list)
                planE[i][j] = value
    #print "LIST :",list

    #print "tempPlan : " , tempPlan[v]
    return tempPlan[v]
def getValue(v,l):
#    print " getValue_RPG Function "

    for i in range(len(l)):
        if(v==l[i][0]):
            return l[i][1]
    return []

def actionPlans():
    actions = copy.deepcopy(getActionList())

    #print actions
    action_plans=[]
    

    for i in range(len(actions)):
        planList =[]
        #for i in range(len(actions)):
        planList.append(unifyPossibleActions(actions[i]))
        #print planList
        #for i in range(len(actions)):
        action_plans.append(applyGTtoPlan(actions[i], planList))


    for i in range(len(action_plans)):
        print action_plans[i]
    print processPlan(action_plans[0])
    return action_plans

def getActionPlans():
    print "getActionPlans"
    return actions_plans


def processPlan(plan):
    print "processPlan Function"
    plan_effects = []
    for i in range(len(plan[2])):
        plan_effects.append(plan[2][i])

    return plan_effects


def insertBB(l):
    t = " ( "
    count = 0
    for i in range(len(l)):
        t += l[i]
        if(count == 0):
            t += " ( "
        elif(i < len(l)-1):
            t += " , "
        else:
            t += " "
        count += 2
    t += " )  )  "
    #print t
    return t


###############################################################################
#                  Relaxed Planning Graph Functions                           #
###############################################################################


def getTarget_RPG(goal1):
    print "getTarget Function "
    target_list =[]
    print goal1

    for i in range(len(beliefList)):
        if((len(goal1)==len(beliefList[i]))and(goal1[0]==beliefList[i][0])):
            target_list.append(beliefList[i])

    print "Target List ",target_list
    return target_list


def intention_main():
    global planBase
    global actionBase
    global actions_plans
    global target
    global goal
    #bl = beliefList
    time = goal_time
    g =[]
    goal = getGoal()

    #planBase = parsePlanFile('planLibrary')
    #print planBase
    #print "Action Base"
    #actionBase  = parseActionFile('actionBase')
    #print actionBase

    #actions_plans = actionPlans()
    heuristic_main()
    indexList = getSortedPlanIndex()
    finalPlanList = allApplicableAfterPruning()

    

    print "FinalPlanList " , len(finalPlanList)
    
    for i in range(len(finalPlanList)):
        print finalPlanList[i]

    final_plans =[]

    print "SORTED INDEX : ",indexList
    for i in range(len(indexList)):
        if(indexList[i][1]<=time):
            print indexList[i][1]
            finalPlanList[indexList[i][0]].append(indexList[i][1])
            final_plans.append(finalPlanList[indexList[i][0]])

    print "final_plans", final_plans
    
    finalPlanList = final_plans

    for i in range(len(finalPlanList)):
        print finalPlanList[i]

    print "****************Final Plan List **********************************"
    
    for i in range(len(finalPlanList)):
        print finalPlanList[i]

    if(finalPlanList==[]):

        for i in range(len(finalPlanList)):
            
            bl = copy.deepcopy(beliefList)

            print "i === ",i

            stack =[]
            c =False
            for j in range(len(finalPlanList[i][2])):

                stack.append(finalPlanList[i][2][j])
            stack.reverse()
            print "Initial Stack "
            print stack
            v = intension(stack, bl, g)
            if(v):
                c = True                
                break
        if(c):

            print " Execution of plan completed with Time ",finalPlanList[i][3]
            print " Belief base is changed to  ",bl
        else:
            print "No plan found with user Specified Time "
    else:
        print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  RPG to generate a plan%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% "

        goal1 = copy.deepcopy(goal)
        del goal1[len(goal)-1]
        print "GOAL INTENTION : ",goal1
        target_list = getTarget_RPG(goal1)
        plans_target_goal = []

        target_list = getTarget_RPG(goal1)
        plans_target_goal = []
        for i in range(len(target_list)):
            print "***************PATH FROM ",target_list[i],"TO ",goal1,"***************"
            target = target_list[i]
            print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"

            # plans_target_goal.append(rpg1(goal1)[0])
            plans_target_goal = relaxedPlanning_main(aFile,pFile,gFile,bFile)

        print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"



        print len(plans_target_goal)
        final_plans_rpg =[]

        for i in range(len(plans_target_goal)):
            print "The sum of %d  %s" % (i+1,plans_target_goal[i])
            print len(plans_target_goal[i])
            print  "goal time : ", goal_time,plans_target_goal[i][len(plans_target_goal)-1]
            if(goal_time >= plans_target_goal[i][2]):
            	print  "goal time : ", goal_time
                final_plans_rpg.append(plans_target_goal[i])
            #print plans_target_goal[i][2]
        plans_target_goal=final_plans_rpg
        print plans_target_goal
        bl = copy.deepcopy(beliefList)
        if(len(plans_target_goal)==1):
#            bl = copy.deepcopy(beliefList)
            temp = copy.deepcopy( plans_target_goal[0])
            del temp[len(temp)-1]
            stack =[]
            c =False
            print len(temp)
            for j in range(len(temp)):
                for i in range(len(temp[j][2])):
                    stack.append(temp[j][2][i])
            stack.reverse()
            print "Initial Stack "
            print stack
            print "Goal :  " ,goal
            v = intension(stack, bl, g)
            print "V ",v
            if(v):
                c = True
                t = plans_target_goal[0][len(plans_target_goal[0])-1]
                print " Execution of plan completed with Time ",t
                print " Belief base is changed to  ",bl
            else:
                print "No plan found with user Specified Time "


        elif(len(plans_target_goal)==0):
            print " There is no plans are possible with the RPG"
        else:
            for i in range(len(plans_target_goal)):
                print "Plan %d  %s " % (i+1,plans_target_goal[i])
                print "length",len(plans_target_goal[i])
            print  (plans_target_goal[1])
            print " There are ", i+1," plans are  availabe for  different places from destination  "
            print " Which Plan to be execute , Enter the plan number "
            number = int(raw_input())
            number -= 1
            #print  (plans_target_goal[number][2])
            temp = copy.deepcopy( plans_target_goal[number])
            del temp[len(temp)-1]
            stack =[]
            c =False
            print len(temp)
            for j in range(len(temp)):
                for i in range(len(temp[j][2])):

                    stack.append(temp[j][2][i])
            stack.reverse()
            print "Initial Stack "
            print stack
            print "Goal " ,goal
            v = intension(stack, bl, g)
            print "V ",v
            if(v):
                c = True
                t = plans_target_goal[number][len(plans_target_goal[number])-1]
                print " Execution of plan completed with Time ",t
                print " Belief base is changed to  ",bl
            else:
                print "No plan found with user Specified Time "

        
            
    f = open('modifiedBeliefBase' , 'w')

    for i in range(len(bl)):
        x = insertBB(bl[i])
        x += "\n"
        f.write(x)
    f.close()

#intention_main()

