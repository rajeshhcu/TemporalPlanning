import copy
#! /usr/bin/python

__author__="rajender"
__date__ ="$May 19, 2009 9:51:22 AM$"

if __name__ == "__main__":
    print "Hello World";

from parseABGP import parseGoalFile
from parseABGP import parsePlanFile

def testForItem(appList , item):

    for i in range(len(appList)):
        for j in range(len(appList[i])):
            if(item == appList[i][j]):
                return appList[i][j+1]
            else:
                j +=1
    return []

def unifyRelevantPlans(g):
    print "Unify Relevant  Plans " , getApplicablePlans()
    appPlanList = getApplicablePlans()
    list =[]
    appList =[]

    for i in range(len(appPlanList)):
        applicablePlanNM = appPlanList[i]
        
        print applicablePlanNM,len(applicablePlanNM)
        for j  in range(len(applicablePlanNM[i])):
            
            if(applicablePlanNM[i][j] == g[j]):
               print "applicablePlanNM : " , applicablePlanNM[i][j] , i
               print "goal :  j" , g,j
               continue
            elif(applicablePlanNM[i][j].isupper()):
                list.append(applicablePlanNM[i][j])
                list.append(g[j])
                appList.append(list)
            else:
                break

        print appList
        planList =[]
        for i in range(len(appPlanList)):
            tempAppPlan = copy.deepcopy(appPlanList[i])
            print tempAppPlan[0],len(tempAppPlan[0])
            print appPlanList ,len(appPlanList)
            for j in range(len(tempAppPlan[0])):
                if(tempAppPlan[0][j].isupper()):
                    #print appList[i] , len(appList[i])
                    tempAppList = appList
                    for l in range(len(tempAppList)):
                        for k in range(len(tempAppList[l])):
                            print "Name",tempAppPlan
                            print "k:",k,k%2
                            print "tempAppList : ",tempAppList[l][k]
                            if(int(k%2)==0):
                                if(tempAppPlan[0][j] == tempAppList[l][k]):
                                    tempAppPlan[0][j] = tempAppList[l][k+1]
                                    print "Name",tempAppPlan
#                        elif(tempAppPlan[0][j] == tempAppList[2]):
#                            tempAppPlan[0][j] = tempAppList[3]
                                
            for j in range(len(tempAppPlan[1])):
                for k in range(len(tempAppPlan[1][j])):
                    if(tempAppPlan[1][j][k].isupper()):
                        t = testForItem(appList, tempAppPlan[1][j][k])
                        #print testForItem(appList, tempAppPlan[1][j][k])
                        if(t != []):
                            tempAppPlan[1][j][k] = t
                            #print tempAppPlan[1][j][k]
                        else:
                            continue

       
            for j in range(len(tempAppPlan[2])):
                for k in range(len(tempAppPlan[2][j])):
                    if(tempAppPlan[2][j][k].isupper()):
                        t = testForItem(appList, tempAppPlan[2][j][k])
                        #print testForItem(appList, tempAppPlan[2][j][k])
                        if(t != []):
                            tempAppPlan[2][j][k] = t
                            #print tempAppPlan[2][j][k]
                        else:
                            continue

            planList.append(tempAppPlan)

        print "Number of Relevant Plans   : ", len(planList)
        
        return planList



def getApplicablePlans():
    print "get Unifying List"
    return applicableList



def unifyPlanLibraryAndGoal(planFile,goalFile):
    print "This is unifyPlanLibraryAndGoal Function "

    g = parseGoalFile(goalFile)

    if((g[len(g)-1].isdigit())or(not g[len(g)-1].isalnum())):
        del g[len(g)-1]
    print " GOAL ", g


    pl = parsePlanFile(planFile)
    global applicableList
    global relevantPlanList
    
    applicableList = []
    applicablePlan =[]

    for i in range(len(pl)):
        tempPN  =  pl[i][0]
        #del tempPN[0]
        print tempPN
        if((tempPN[0] == g[0]) and (len(tempPN) == len(g))):
            applicablePlan = pl[i]
            applicableList.append(applicablePlan)
            print "APPLICABLE LIST ",applicableList
    if(applicableList ==[]):
        print "applicable List : ",applicableList
        return False
    else:
        print  getApplicablePlans()
        print len(applicableList)

        relevantPlanList = unifyRelevantPlans(g)

        print "Relevant Plans after Unifying Plan Library and Goal "
        print "Relevant Plans : " , relevantPlanList
        for j in range(len(relevantPlanList)):
            print "Plan  ", j+1 ,": "  ,relevantPlanList[j]

    return True

#unifyPlanLibraryAndGoal('planLibrary', 'goal')
def getRelevantPlan():
    print " getRelevantPlan Function "
    return relevantPlanList

##############################################################################
#****************************APPLICABLE PLAN ********************************#
##############################################################################

def parseBL():
    temp =[]
    for i in range(len(bl)):
        temp .append(bl[i][0])
    return temp
def testforUnifyRPLandBL(p):
    print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
    print " testforUnifyRPLandBL Function"
    print bl
    print"&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"

    t = False
    for i in range(len(bl)):
        #print "**********************Outter For Loop**********************"
        tempB = bl[i]
        #print tempB , " matching for ",p

        if(len(tempB) == len(p)):
            #print " tempB : ", tempB,"precondition :" ,p
            for j in range(len(tempB)):
                #print "**********************************Inner For Loop***********"
                if(tempB[j] == p[j]):
                    #print tempB[j]
                    #print p
                    t = True
                    continue
                else:
                    t = False
                    break
        if(t == True):
             return t

    return False



def getApplicablePlan():
    print " getApplicablePlan Function"
    for i in range(len(rpl)):
        preconditionList = rpl[i][1]
        print preconditionList
        t = False
        for j in range(len(preconditionList)):
            precondition = preconditionList[j]
            print precondition
            if(testforUnifyRPLandBL(precondition)):
                t = True
                continue
            else:
                t = False
                break
        if(t== True):
            applicablePlans.append(rpl[i])
            print applicablePlans


unifyPlanLibraryAndGoal('planLib', 'goal')
