#! /usr/bin/python

__author__="rajender"
__date__ ="$May 19, 2009 6:57:51 AM$"

if __name__ == "__main__":
    print "Converting FOL of Belief , Plans , Goal and Actions  to List ";



def parseBelief(s):
        newlist = []
        tempPlan = []
        length = len(s)

        for i in range(length):
            if((s[i]=='(') or (s[i]==')') or (s[i]==',')):
               continue
            else:

                newlist.append(s[i])

        tempPlan.append(newlist)
        return tempPlan

def parsePrecondition(p):
    preconditionList =[]
    precondition = []
    length = len(p)

    for i in range(length):

        if(p[i] == ')'):
            preconditionList.append(precondition)
            precondition = []
        elif((p[i] == ',') or (p[i] == '(')):
            continue
        else:
            precondition.append(p[i])

    return preconditionList



def parsePlanLibrary(s):
    planName =[]
    planPrecondition = []
    planEffects = []
    plan = []


    planName = s[0]
    planName = planName.split()
    planName = parseBelief(planName)
    planName  = planName[0]

    temp = s[1].split('<-')

    planPrecondition = temp[0].split()
    planPrecondition = parsePrecondition(planPrecondition)

    planEffects = temp[1].split()
    planEffects = parsePrecondition(planEffects)


    del planEffects[len(planEffects)-1]


    plan.append(planName)
    plan.append(planPrecondition)
    plan.append(planEffects)

    return plan



def parseBeliefFile(filename):
    print "paresBeliefFile Function "
    f = open(filename)

    beliefs = f.readlines()
    g =open(filename)

    global beliefList
    beliefList = []
    for i in range(len(beliefs)):

        s = g.readline()
        s = s.split()         
        beliefList.append(parseBelief(s)[0])

    return beliefList


def parsePlanFile(filename):
    print "parsePlanFile Function "
    g = open(filename)
    pl = g.readlines()
    length = len(pl)
    global planList
    planList = []
    f = open(filename)
    for j in range(length):
        plans = f.readline()
        plans = plans.split(':')

        plan = parsePlanLibrary(plans)
        planList.append(plan)
    g.close()
    f.close()

    return planList


def parseActionFile(fileName):
    print "parseActionFile Function"
    f = open(fileName)

    actions = f.readlines()
    g =open(fileName)

    global actionList
    actionList = []
    for i in range(len(actions)):

        s = g.readline()
        s = s.split()
        actionList.append(parseBelief(s)[0])

    return actionList


def parseGoalFile(fileName):
    print "parseGoalFile Function"
    f = open(fileName)

    goal = f.readlines()
    g =open(fileName)

    global goalList
    goalList = []
    for i in range(len(goal)):

        s = g.readline()
        s = s.split()
        goalList.append(parseBelief(s)[0])

    return goalList[0]
def getGoal():
    print "getGoal Function "
    return goalList[0]
def getBeliefList():
    print "getBeliefList Function "
    return beliefList
def getPlanList():
    print "getPlanList Function "
    return planList
def getActionList():
    print "getActionList Function "
    return actionList