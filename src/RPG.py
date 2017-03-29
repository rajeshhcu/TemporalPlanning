
#! /usr/bin/python


import copy
import os

from parseABGP import parseActionFile
from parseABGP import parsePlanFile
from parseABGP import parseGoalFile

from parseABGP import parseBeliefFile


global final_path
def getTime_RPG(a):
    #print "This is getTime Function "

    for i in range(len(actionBase)):
        temp = copy.deepcopy(actionBase[i])

        del temp[len(actionBase[i])-1]

        if(temp==a):
            print  actionBase[i][len(temp)]
            return float(actionBase[i][len(temp)])
    return -1


def minimumCost_RPG(mv,ind):
    #print "minimumCost Function "

    min = 0
    for i in range(len(mv)):
        if(i==0):
            min = float(mv[0])
            value = 0
        else:
            if(min > float(mv[i])):
                min = float(mv[i])
                value = i
    ind.append(value)
    return min



def minCost_RPG(g,p):
    print "minCost Function "
    print "New Goal",g

    planList =[]
    plan =[]
    tr =[]
    if(target == g):
        print " New Goal is equal to Target "
        return 0
    elif(g == []):
        return []
    else:

        actionlist = selectActions_RPG(g)
        for i in range(len(actionlist)):
            planList.append(unifyPossibleActions_RPG(actionlist[i]))
        for i in range(len(actionlist)):
            plan.append(applyGTtoPlan_RPG(actionlist[i], planList))
        for i in range(len(plan)):
            r1 = getAction_RPG(plan[i], g)
#            print "Action Name with Goal ( r1) "
#            print r1
#            print g
#            print "TR : "
#            print tr
            if(r1 != []):
                tr.append(r1)

#        print " Actions  that satifies the goal :"
#        print tr

        min =[]
        minValue =[]

        temp =[]

        index=[]
        print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        print "Applicable Action List "
        for i in range(len(tr)):
        	print tr[i]
        print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
        for i in range(len(tr)):
            temp1 =[]
            t = minCost_RPG(getNewGoal_RPG(tr[i], g),temp1)
            #print "t value  : ",t
            if(t==0):
                t = True
            if((t==[])or (t == False)) :
#                print " (((((((((((((((((((((IF STATEMENT )))))))))))))))))))))"
                #temp1=[]
                return False


            else:
                if(t==True):
                    t=0
#                print " (((((((((((((((((((((ELSE STATEMENT )))))))))))))))))))))"
                minValue.append(float(t) + getTime_RPG(tr[i][0]))
                temp1.append(tr[i])
                temp.append(temp1)
#                print "Temp1 Value : "
#                print temp1
#                print "Temp Value : "
#                print temp
        if(len(minValue)>1):
            min = float(minimumCost_RPG(minValue,index))
#            print "INDEX : ",index[0]
#            print temp
#            print  "PREVIOUS PATH ",p
			#print "Path "
            p.append(temp[index[0]])
#            print "PATH  : ", p

        elif(len(minValue) ==0 ):
#            print "len(minValue) : ", len(minValue)
#            print "PATH : ",p
            return False
        else:
            min = float(minValue[0])
#            print "INDEX : ",index
#            print temp
#            print  "PREVIOUS PATH ",p
            p.append(temp[0])
#            print "PATH  : ", p
    return float(min)




def rpg1(g):

    # Input Goal
    # output plan or []

    #action_list = []

    # Selects  all the Actions Matching with the Goal


    action_list = selectActions_RPG(g)

#    print "ACTIONLIST : "
#    print action_list



    planList=[]

    # Unifies the actions with the planLibrary
    # This is important  because to know the effects of the action after completion

    for i in range(len(action_list)):
        planList.append(unifyPossibleActions_RPG(action_list[i]))

    for i in range(len(planList)):
        print planList[i]
    #time.sleep(6)

    plan =[]
    index =[]
    # After getting the plans
    # We need to substitute the ground terms in place of Variables
    # Following code does this action
    # Unified plans with the actions are available in the "plan" variable

    for i in range(len(action_list)):
        plan.append(applyGTtoPlan_RPG(action_list[i], planList))

    for i in range(len(plan)):
        print plan[i]


#    print "PLANLIST : "
#    print planList
#    print len(planList)
#    print "PLAN:"
#    print plan
#    print len(plan)


    tr =[]
    for i in range(len(plan)):
        r1 = getAction_RPG(plan[i], g)
#        print "Action Name with Goal "
#        print r1
#        print len(r1)
#        print g

        if(r1!=[]):
            tr.append(r1)

#    print "Tempory Actions :"
#    print tr

	print"Applicable Action List "
	for i in range(len(tr)):
		print tr[i]
    plan =[]
    min =[]
    minValue =[]
    p=[]
    temp =[]
    global final_path
    final_path =[]
    for i in range(len(tr)):
        temp1 =[]
        #print  "****************************************************************"
        #print "********************" , i ,"*************************************"
        #print "Processing Path : "
        #print tr[i]
        #print "Temporary Action before Append :"
        #print p
        #print "GOAL", g
        t = minCost_RPG(getNewGoal_RPG(tr[i], g),temp1)
        s=copy.deepcopy(t)
        #print "T : ",t
        if(t==0):
            t = True
        if(t==False):
            #print "if statement : ",t
            continue
        else:
        #time.sleep(4)
        #print "TEMP1 in For loop : ", temp1

        #time.sleep(1)
            #if(t==True):
             #   t=0

            if(t == 0):
                #print "If Statement in main RPG"
                
                minValue.append(float(s) + getTime_RPG(tr[i][0]))
#            print "tr[i] : "
#            print tr[i]
                temp1.append(tr[i])
                temp.append(temp1[0])

                #print "Plans after Processing "
#            #for lp in range(len(temp1)):
                #print "TEMP1 VALUE ",temp1[0]
#            #for lp in range(len(temp)):
                #print "ONE OF THE COMPLETE PATH ",temp

            else:
                #print "Else Statement in main RPG"
                minValue.append(float(s) + getTime_RPG(tr[i][0]))
                temp1.append(tr[i])
                temp.append(temp1)

                #print "Plans after Processing "
#            #for lp in range(len(temp1)):
                #print "TEMP1 VALUE ",temp1
#            #for lp in range(len(temp)):
                #print "ONE OF THE COMPLETE PATH ",temp
#
#        #time.sleep(6)
#        print "****************************************************************"


    print "*********************************************************"
    print " POSSIBLE PLANS TO REACH THE GOAL "
    for i in range(len(temp)):
        print temp[i],minValue[i]
    print "*********************************************************"



    if(len(minValue)>1):
        min = float(minimumCost_RPG(minValue, index))
        print  "FINAL PATH ",temp[index[0]]
	temp[index[0]].append(min)
	os.remove('/home/rajesht/Desktop/TemporalPlanning1/src/test')
	fileHandle = open ( 'test', 'a' )
        fileHandle.write(repr(temp[index[0]]))
        fileHandle.close() 
        print min
        final_path.append(temp[index[0]])
	
		 
	
	
	
    elif(len(minValue)==1):
        min = float(minValue[0])
#        print temp
        #print  "PREVIOUS PATH 0 ",p
        temp1.append(min)

        p.append(temp1)
        print  "FINAL PATH  ",p
        final_path.append(temp[index[0]])
    else:
        print " No plans are generated using RPG "
        final_path.append([])

    #print " Minimum Time  to reach Goal is : " , min
    
    
    
    
    return  final_path[0]

def selectActions_RPG(g):
    #print " selectActions Function"
    #print g
    possibleActions =[]
    for i in range(len(actionBase)):
        if(searchAction_RPG(actionBase[i],g)):
            possibleActions.append(actionBase[i])
        else:
            continue
    return possibleActions

def searchAction_RPG(a,g):
    #print " searchAction Function a g:  ", len(a),len(g)
    #print "Goal",g
    value = False
    for i in range(len(a)):
        if(g[1]==a[i]):
#            print a[i]
            value = True
    return value

def unifyPossibleActions_RPG(a):
    #print "Unify Actions with plans "

    unifyPlanList =[]
    for i in range(len(planList)):
        if((len(a)-1)==len(planList[i][0])):
            if(a[0]==planList[i][0][0]):
                unifyPlanList.append(planList[i])
    #print "unifyPlanlist : ",unifyPlanList[0]
    return unifyPlanList[0]

def applyGTtoPlan_RPG(a,p):
#    print " applyGTtoPlan_RPG Function "
    l =[]
    list =[]
    condition=False
    tempPlan = copy.deepcopy(p)

#    print a
#    print tempPlan

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
#    print list


    return tempPlan[v]

def getValue_RPG(v,l):
#    print " getValue_RPG Function "

    for i in range(len(l)):
        if(v==l[i][0]):
            return l[i][1]
    return []


def getAction_RPG(p,g):

    #print " This is getAction_RPG Function "
    #print "plan name : ",p
    rpgAction = []
    pe = p[2]

    value = True

    for i in range(len(pe)):


        if((pe[i][0] == "+") and (len(g)== ((len(pe[i]))-1)) ):

            tempPE = copy.deepcopy(pe[i])
#            print tempPE
            del tempPE[0]
#            print tempPE

            for j in range(len(tempPE)):

                if(tempPE[j] == g[j]):
                    value = True
                elif(tempPE[j]=="+"):
                    continue
                else:

                    rpgAction =[]
                    value = False
                    break
    if(value):

        rpgAction.append(p)


#    print "rpgAction in get Function :"
#    print rpgAction

    if(rpgAction!=[]):
        #print "rpgAction !=[] :  " , rpgAction
        return rpgAction[0]

    else:
        #print "rpgAction ==[] :  " , rpgAction
        return rpgAction




def getNewGoal_RPG(p,g):
    # This function takes plan  and previous goal as the input and returns
    #  the new goal from where last goal  can be achievable
    #  The  fact in the precondition is negated in  the effects part.
    #print " getNewGoal Function "
    #print g
#
    pp = p[1]
    pe = p[2]
    #print "Precondition :"
    #print pp
    #print "Effect :"
    #print pe
    for i in range(len(pp)):

        if(len(pp[i])==len(g)):
            if(pp[i][0] == g[0]):
                newgoal = pp[i]
                #print "newgoal : " ,newgoal
    for i in range(len(pe)):
        if((len(pe[i])-1) == len(newgoal)):
            if(pe[i][0]=="-"):

                for j in range(len(pe[i])):
                    if(pe[i][j]=="-"):
                        continue
                    elif(pe[i][j]==newgoal[j-1]):
                        v=True
                    else:
                        v = False
                if(v ):
                    break
                else:
                    newgoal =[]

    return newgoal


def getTarget_RPG(goal1):
    #print "getTarget Function "
    target_list =[]
    #print goal1

    for i in range(len(beliefList)):
        if((len(goal1)==len(beliefList[i]))and(goal1[0]==beliefList[i][0])):
            target_list.append(beliefList[i])

    #print "Target List ",target_list
    return target_list

def relaxedPlanning_main(actionFile,planFile,goalFile,beliefFile):
    print "Relaxed Planning Graph Main "
    global path
    path =[]
    global actionBase
    global planList
    global beliefList


    global target



    actionBase = parseActionFile(actionFile)
    planList = parsePlanFile(planFile)
    beliefList = parseBeliefFile(beliefFile)
    print " Plan Base \n \n \n"
    for i in range(len(planList)):
        print planList[i]

    print " \n\n\n Belief Base \n\n"
    for i in range(len(beliefList)):
        print beliefList[i]

    print "\n\n Action Base \n"
    for i in range(len(actionBase)):
        print actionBase[i]

    print "\n Goal Element \n"
    goal1 = copy.deepcopy(parseGoalFile(goalFile))
    del goal1[len(goal1)-1]
    print goal1



# Following Code is to Extract the Relaxed Plan ( All Possible plans)
# that can be applicable to  a given goal
#
#goal =['at' , 'losangels']
    #print goal1



    target_list = getTarget_RPG(goal1)
    plans_target_goal = []
    for i in range(len(target_list)):
        print "***************PATH FROM ",target_list[i],"TO ",goal1,"***************"
        target = target_list[i]
        #print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"

        plans_target_goal.append(rpg1(goal1))


        print "***********************************************************************"

    
    for i in range(len(plans_target_goal)):
        if(plans_target_goal[i]!=[]):
            #print plans_target_goal[i]
            plans_target_goal[i] = removeExtraBrackets(plans_target_goal[i])
            path.append(plans_target_goal[i])
            #print "after removing Brackets"
            #print plans_target_goal[i]
    #print "Plans geneerated by RPG "
    #for i in range(len(path)):
     #   print path[i]
    return path


def removeExtraBrackets(p):
    #print "removeExtraBrackets Function "    
    result =[]
    if(p!=[]):
        condition = True
        result.append(p[len(p)-1])
        del p[len(p)-1]        
    else:
        condition = False

    if(len(p)==3):
        result.append(p)
    else:
        while condition:           
            sel = (p.pop())
            if(len(sel)==3):
                result.append(sel)
            else:
                p = sel            
            if(p ==[]):
                condition = False
    result.reverse()
    
    return result

#print"RPG _ MAIN"
#relaxedPlanning_main('actionBase','planLibrary','goal','beliefBase')

   


