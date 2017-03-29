#! /usr/bin/python

__author__="rajender"
__date__ ="$May 20, 2009 7:54:04 AM$"

if __name__ == "__main__":
    print "Hello World";


import copy
from parseABGP import getActionList
from testParseFunction import applicablePlans
from applicablePlans import bl
#from time import sleep
from testParseFunction import beliefList


def extraPlan(p,valueList,v):
    planList = []


    for ii in range(len(valueList)):
        tp =[]
        tp = copy.deepcopy(p)
        print tp
        print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
        print "valueList Item Name ",valueList[ii]
        print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
        pn = tp[0]
        pp = tp[1]
        pe = tp[2]
        plan =[]
        for i in range(len(pn)):
            if((pn[i].isupper() )and pn[i]==v):
                pn[i] = valueList[ii]
        for i in range(len(pp)):
            for j in range(len(pp[i])):
                if(pp[i][j].isupper() and (pp[i][j]==v)):
                    pp[i][j] = valueList[ii]
        for i in range(len(pe)):
            for j in range(len(pe[i])):
                if(pe[i][j].isupper() and (pe[i][j]==v)):
                    pe[i][j] = valueList[ii]
        print tp
        print p
        plan.append(pn)
        plan.append(pp)
        plan.append(pe)
        planList.append(plan)

    print planList
    return planList


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


def unifyForGT(variable):
    print "unifyForGT function "
    global listUnify
    global tal
    listUnify =[]
    list = []
    list1 =[]

    tbl = bl
    tal = getActionList()

    for i in range(len(tal)):
        del tal[i][len(tal[i])-1]

    print "**********************BL and AL*****************"
    print tbl
    print tal
    print "*****************************************"
    for i in range(len(variable)):
        tv  = variable[i]
        for j in range(len(tbl)):
#            print "tv[0] , tbl: " , tv[0] , tbl[j]
            if((tv[0] == tbl[j][0]) and (len(tv) and len(tbl[j])) ):
#                print "tv , tbl: " , tv , tbl[j] , len(tv),len(tbl[j])
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

    if(listUnify==[]):
        for i in range(len(variable)):
            tv  = variable[i]
            for j in range(len(tal)):
#            print "tv[0] , tbl: " , tv[0] , tbl[j]
                if((tv[0] == tal[j][0]) and (len(tv) and len(tal[j])) ):
#                print "tv , tbl: " , tv , tbl[j] , len(tv),len(tbl[j])
                    test = False
                    for k in range(len(tv)):
                        if(tv[k]==tal[j][k]):
                            test = True
                            continue

                        elif((tv[k].isupper())and test):
#                        print "(tv[k].isupper())and test) "
                            list1.append(tv[k])
                            list1.append(tal[j][k])
                            listUnify.append(list1)
                            list1 =[]
#                        print tbl[j] , tv,

#                        print " List :" , list
                        else:
                            test = False
                            break


    listUnify = removeDuplicates(listUnify)
    print " list :" , listUnify
    return listUnify




def searchForList(pp):
    list = []
    for i in range(len(pp)):
        #tpp = pp[i]
        for j in range(len(pp[i])):
            if((pp[i][j].isupper())):
                list.append(pp[i])
            else:
                continue

    return list
def makeVariableIntoGT(p):
    print "makeVariableIntoGT Function "
    bl = beliefList
    pp = p[1]
    pe = p[2]
    global listPP
    global listPE
    listPP = []
    listPE =[]
    variablePPList =[]
    variablePEList=[]

    if( (testForGTInPP(pp))):
        variablePPList = searchForList(pp)
        print"******************************"
        print variablePPList
        print "******************************"
    print "testForGTInPP(pp) " , testForGTInPP(pp)
    if( (testForGTInPE(pe))):
        variablePEList = searchForList(pe)
        print"************PEList******************"
        print "variablePEList ",variablePEList
        print "******************************"
    print "testForGTInPP(pe)" ,testForGTInPP(pe)
    if(variablePPList!=[]):
        listPP = unifyForGT(variablePPList)
    if(variablePEList != []):
        print "if(variablePEList != [])"
        listPE = unifyForGT(variablePEList)
        print "listPE : ",listPE

    print "search for List ", searchForList(pe)
    print listPP

def testForGTInPN(pn):
    #print " TestForGroundTermsInPlanName Function "
#    print pn
    for i in range(len(pn)):

        if(pn[i].isupper()):
            return True


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


def generateExtraPlan(p,v,value):
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

#    print " This is Generate Extra Plan Function"
#    print plan
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

#    Following code  returns all the variables
#    input = [['P', 'losangels'], ['P', 'phonex']]
#    output will be  ['P']

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
                    #print variableItems


    for j in range(len(variableItems)):
        stack1 =[]
        for i in range(len(list)):
            #for k in range(len(list[i])):
            if(variableItems[j] == list[i][0]):
                stack1.append(list[i][1])
        stack.append(stack1)
    print stack





    for j in range(len(variableItems)):
#    for i in range(len(app)):
        for k in range(len(stack[j])):
                tapp = copy.deepcopy(app)
                if( (testForGroundTermsInPlan(tapp))):

#                    print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
#                    print app
#                    print testForGroundTermsInPlan(app)
                    #print app[i]
                    newPlanList.append(generateExtraPlan(tapp, variableItems[j], stack[j][k]))

#                    print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
                else:
                    print "In else stm   j k " , j ,k
                    continue
#                    print testForGroundTermsInPlan(app[i])



    print " New Extended  Plan List"
    print newPlanList
    return newPlanList






ap = applicablePlans
#global listUnify
l =[]

for i in range(len(ap)):
    if(not testForGroundTermsInPlan(ap[i])):
        l.append(ap[i])
print "List of Plans "
print l
for i in range(len(l)):
    print l[i]

print "applicable Plans"
print ap
for i in range(len(ap)):
    p = ap[i]
    pn = p[0]
    pp = p[1]
    pe = p[2]

    print "ap :"
    print ap[i]
    if(testForGroundTermsInPlan(p)):
        print " Plan not having Ground Terms "
        makeVariableIntoGT(p)

        l1 = listofPossiblePlansAfterUnify(p)
        print "l1:",l1
        if(l1!=[]):
            for j in range(len(l1)):
                print " Before append"
                print l
                l.append(l1[j])
                print "l in l1"
                print l

    else:
        print " Plan have  Ground Terms"
        #l.append(p)
    print "l : ",len(l)
    print l



print "l",l
global extendedAppPlans
extendedAppPlans = l
print "************************************************************************"
print "******************Extended Applicable Plans*****************************"
for i in range(len(extendedAppPlans)):
    print extendedAppPlans[i]
print "************************************************************************"


print "************************************************************************"
print "******************Extended Applicable Plans*****************************"
for i in range(len(extendedAppPlans)):
    print extendedAppPlans[i]
print "************************************************************************"

#discardUnnecessaryPlan(extendedAppPlans)
