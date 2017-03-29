
__author__="rajender"
__date__ ="$May 19, 2009 6:56:42 AM$"

if __name__ == "__main__":
    print "Temporal Planning ";


from applicablePlans import applicablePlan_Main
from input import gFile
from input import goal
from input import actionBase
from input import beliefList
from input import planList
from input import *
from input import pFile
from intension import intention_main
from relevantPlans import unifyPlanLibraryAndGoal
from relevantPlans import *
from applicablePlans import *
from substituteGroundTerms import *
from intension import *


print "Temporal Planning "
print "*********************************************************"
print "*****************Belief Base*****************************"
for i in range(len(beliefList)):
    print beliefList[i]
print "*********************************************************"

print "*****************Plan Library*****************************"
for i in range(len(planList)):
    print planList[i]
print  "********************************************************"

print "*****************Action Base*****************************"
for i in range(len(actionBase)):
    print  actionBase[i]
print "*********************************************************"

print "*****************Goal************************************"
print goal
print "**********************************************************"

print "*************************Relevant Plans *******************"

condition = unifyPlanLibraryAndGoal(pFile,gFile)

if(condition):
    print "Relevant Plans are obtained "
    print getRelevantPlan()
    applicablePlan_Main(getRelevantPlan(),beliefList)

    applicablePlans = getAllApplicablePlans()

    extendedPlans(applicablePlans,actionBase)

    extendedApplicablePlans = (getExtendedPlans())

    print len(extendedApplicablePlans)

    for i in range(len(extendedApplicablePlans)):
        print extendedApplicablePlans[i]
    
    intention_main()

else:
    print "No relevant Plans are there for give Goal "
    intention_main()
