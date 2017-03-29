#from input import beliefList
import copy
#! /usr/bin/python

__author__="rajender"
__date__ ="$May 19, 2009 4:40:16 PM$"

if __name__ == "__main__":
    print "Hello World";


#from parseABGP import getBeliefList
#from relevantPlans import getRelevantPlan

   
def testforUnifyRPLandBL(p):
#    print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
#    print " testforUnifyRPLandBL Function"
#    print bl
#    print"&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"

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

def testForGTInPP(pp):
    #print "TestForGroundTermsInPlanPrecondition Function "
#    print pp

    for ip in range(len(pp)):
        planPrecond = pp[ip]
        for ipp in range(len(planPrecond)):
#            print planPrecond[ipp]
            if(planPrecond[ipp].isupper()):
#                print "planPrecond[ipp].isupper() ",planPrecond[ipp].isupper()
                return True

def searchForList(pp):
    print "searchForList"
    list = []
    for i in range(len(pp)):
        #tpp = pp[i]
        for j in range(len(pp[i])):
            if((pp[i][j].isupper())):
                list.append(pp[i])
            else:
                continue
    print list
    return list
def unifyForGT(variable):
    print "unifyForGT function "
    global listUnify
    listUnify =[]
    list = []
    list1 =[]

    tbl = bl


    print "**********************BL*****************"
    print tbl
    print "*****************************************"
    for i in range(len(variable)):

        tv  = variable[i]
        for j in range(len(tbl)):
            print "tv[0] , tbl: " , tv[0] , tbl[j],len(tv) , len(tbl[j]),len(tbl)
            if((tv[0] == tbl[j][0]) and (len(tv) == len(tbl[j])) ):
                print "tv , tbl: " , tv , tbl[j] , len(tv),len(tbl[j])
                test = False
                for k in range(len(tv)):
                    if(tv[k]==tbl[j][k]):
                        test = True
                        continue

                    elif((tv[k].isupper())and test):
#                        print "(tv[k].isupper())and test) "
                        list1.append(tv[k])
                        list1.append(tbl[j][k])
                        listUnify.append(list1)
                        list1 =[]
#                        print tbl[j] , tv,

#                        print " List :" , list
                    else:
                        test = False
                        break


    
    listUnify = removeDuplicates(listUnify)
    print " listUnify :"
    for i in range(len(listUnify)):
        print listUnify[i]
    return listUnify

def generateExtraPlan(p,v,value):
    print "generateExtraPlan Function "
    pn = p[0]
    pp = p[1]
    pe = p[2]
    plan =[]
    for i in range(len(pn)):
        if((pn[i].isupper() )and pn[i]==v):
            pn[i] = value
    for i in range(len(pp)):
        for j in range(len(pp[i])):
            if(pp[i][j].isupper() and (pp[i][j]==v)):
                pp[i][j] = value
    for i in range(len(pe)):
        for j in range(len(pe[i])):
            if(pe[i][j].isupper() and (pe[i][j]==v)):
                pe[i][j] = value

    plan.append(pn)
    plan.append(pp)
    plan.append(pe)

    print " This is Generate Extra Plan Function"
    print plan
    return plan

def listofPossiblePlansAfterUnify(app):
#    This Function adds plans with all the possibilites
#    of the Variable
    newPlanList = []
#    app = applicablePlans

    stack=[]

    variableItems =[]


    list = listUnify
    print "listUnify : ",listUnify
    print len(list)
#    Following code  returns all the variables
#    input = [['P', 'losangels'], ['P', 'phonex']]
#    output will be  ['P']
    variable_stack =[]
    for i in range(len(list)):
        if(list[i][0] in variable_stack):
            continue
        else:
            variable_stack.append(list[i][0])

    print variable_stack


    variable_GT =[]

    for j in range(len(variable_stack)):
        tempGT =[]
        for i in range(len(list)):
            if(list[i][0] == variable_stack[j]):
                if(not (list[i][1] in tempGT)):
                    tempGT.append(list[i][1])
        variable_GT.append(tempGT)

    print  variable_GT


    for i in range(len(list)):
        if(variableItems == []):
            variableItems.append(list[i][0])

        else:

            for j in range(len(variableItems)):

                if(variableItems[j]==list[i][0]):

                    v1 = False
                    continue
                else:
                    v1 = True


            if(v1):
              variableItems.append(list[i][0])
              #print "variable Items  ",variableItems


    for j in range(len(variableItems)):
        stack1 =[]
        for i in range(len(list)):
            #for k in range(len(list[i])):
            if(variableItems[j] == list[i][0]):
                stack1.append(list[i][1])
        stack.append(stack1)
   
    print "Stack "
    for i in range(len(stack)):
        print stack[i]


    variableItems = variable_stack
    stack = variable_GT
    print "variableItems : ",variableItems
    print " stack " , stack

    tappList=[]
    tappNewList =[]
    tappList.append(app)
    for j in range(len(variableItems)):
        tappNewList =[]
        for i in range(len(tappList)):


            for k in range(len(stack[j])):
                    tapp = copy.deepcopy(tappList[i])
                    if( (testForGroundTermsInPlan(tapp))):

#                    print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
#                    print app
#                    print testForGroundTermsInPlan(app)
                    #print app[i]
                        tappNewList.append(generateExtraPlan(tapp, variableItems[j], stack[j][k]))

#                    print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
                    else:
                        print "In else stm   j k " , j ,k
                        continue

        tappList = copy.deepcopy(tappNewList)


    print "tappList"
    for i in range(len(tappList)):
        print tappList[i]







    


    print " New Extended  Plan List"
    print tappList
    return tappList

def testForGroundTermsInPlan(p):
    #print " TestForGroundTermsInPlan Function "

    pn = p[0]
    pp = p[1]
    pe = p[2]

    pnResult = testForGTInPN(pn)
#    print "pnResult : ",pnResult
    ppResult = testForGTInPP(pp)
#    print "ppResult : ",ppResult
    peResult = testForGTInPE(pe)
#    print "peResult : ",peResult

    if(pnResult  or  ppResult or  peResult):
        return True
    else:
        return False

def testForGTInPN(pn):
    #print " TestForGroundTermsInPlanName Function "
#    print pn
    for i in range(len(pn)):

        if(pn[i].isupper()):
            return True


    return False

def testForGTInPE(pe):
    #print "TestForGroundTermsInPlanEffects  Function "

    for ip in range(len(pe)):
        planEffect = pe[ip]
        for ipp in range(len(planEffect)):
#            print planEffect[ipp]
            if(planEffect[ipp].isupper()):
                return True
#            else:
#                #print " No Ground Term in Plans Effects"
#                return False

    return False


def removeDuplicates(list):
    print "removeDuplicates " , len(list)

    list1 = []

    for i in range(len(list)):
        temp = list[i]

#        print list[i]
        x = selectIndexToDelete(i, temp, list,list1)
#        print x
        if(x):
            continue
        else:
            list1.append(list[i])
#        print "List1 : ",list1

#      print list
    print "removeDuplicates Function : ", list1
    return list1

def selectIndexToDelete(i,temp,list,list1):


        if(list1 == []):
            return False
        else:
            t = False
            for ip in range(len(list1)):
#                print "list1 in for loop",list1[ip]

                for j in range(len(temp)):
#                    print "list1[ip]",list1[ip]
                    if(temp[j] == list1[ip][j]):
                        t = True
#                        print temp[j],list1[ip][j],t
                        continue
                    else:
                        t = False
                        continue
            if(t ==True):
                return True
            else:
                return False

def getApplicablePlan():
    print " getApplicablePlan Function"
    global listPP
    listPP = []

    rpl1 = copy.deepcopy(rpl)
    for i in range(len(rpl1)):
        app = copy.deepcopy(rpl1[i])
        if(testForGTInPP(rpl1[i][1])):
            print "Precondition is not having Ground Term"
            variablePPList = searchForList(rpl1[i][1])
            print variablePPList
            if(variablePPList!=[]):
                listPP = unifyForGT(variablePPList)
            print listPP

            l1 = listofPossiblePlansAfterUnify(app)

            for j in range(len(l1)):
                rpl1.append(l1[j])
    for i in range(len(rpl1)):
        
        preconditionList = rpl1[i][1]
        print preconditionList
        t = False
        for j in range(len(preconditionList)):
            precondition = preconditionList[j]
#            print precondition
            if(testforUnifyRPLandBL(precondition)):
                t = True
                continue
            else:
                t = False
                break
        if(t== True):
            applicablePlans.append(rpl1[i])
#            print applicablePlans



def  applicablePlan_Main(relevantP,beliefL):
    print "applicablePlan_Main Function"

    global rpl
    global bl
    global applicablePlans
    applicablePlans =[]
    rpl = relevantP
    bl = beliefL
    
    print "***********************************************************************"
    print "**********************Applicable Plan Function************************* "
    print "************************************************************************"

    for i in range(len(rpl)):
        print rpl[i]

    print "**********************Belief Base***************************************"

    for i in range(len(bl)):
        print bl[i]
    print "************************************************************************"
    getApplicablePlan()
    print "***********************************************************************"
    print "**********************Applicable Plans Function************************* "
    print len(applicablePlans)
    for i in range(len(applicablePlans)):
        print applicablePlans[i]

    print "************************************************************************"


def  getAllApplicablePlans():
    return applicablePlans

#applicablePlan_Main(getRelevantPlan(), beliefList)



#global listPP
#listPP = []
#
#rpl1 = copy.deepcopy()
#for i in range(len(rpl1)):
#    app = copy.deepcopy(rpl1[i])
#    if(testForGTInPP(rpl1[i][1])):
#        print "Precondition is not having Ground Term"
#        variablePPList = searchForList(rpl1[i][1])
#        print variablePPList
#        if(variablePPList!=[]):
#            listPP = unifyForGT(variablePPList[0])
#        print listPP
#
#    print listofPossiblePlansAfterUnify(app)
