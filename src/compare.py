import copy
from input2 import *
from input2 import seedPlan
from input2 import domainList
from input2 import beliefs
from input2 import planMetric
from input2 import target

print "Temporal Planning under uncertainty"
print "********************************************************"
print "***********************Seed Plan************************"
global newPlan
newPlan = []	
print "n",seedPlan[0],seedPlan[0][(len(seedPlan[0])-2)]
for i in range(len(seedPlan)) :
           if(seedPlan[i][(len(seedPlan[i])-2)]==seedPlan[0][6]):
	  	    newPlan.append(seedPlan[i][1:(len(seedPlan[i])-2)])
	   else:	    
	            newPlan.append(seedPlan[i][1:(len(seedPlan[i])-1)])
print newPlan                	


print "**********************Domain List************************"
for i in range(len(domainList)):
     print domainList[i]
		
print "***********************Intials****************************"		
for i in range(len(beliefs)):
	print beliefs[i]
	
print "**********************Plan Metric**************************"
print planMetric
	
print "************************Target*****************************"
for i in range(len(target)) :
	print target



global reqList
global reqList1
global reqList2
reqList = []	
reqList1 = []
reqList2 = []
def compare(np,dl):
    print "dl",dl	
    for i in range(len(np)):
           for j in range(len(dl)):
                   if(dl[j][0]==np[i]):
                         l = i+1
                         if(dl[j][1]==np[l]):
		              l = l+2		 
			      if(dl[j][3]==np[l] or len(dl[j])==6):
                                  for k in range(len(dl[j])) :
				              reqList.append(dl[j][k])
                               			   
			      #else:
				#  for k in range(len(dl[j])) :			          
                                 #       reqList.append(dl[j][k])    
				 		 
    reqList1.append(reqList[:len(dl[0])])
    reqList2.append(reqList [ len(dl[0]) : 2*len(dl[0])])
    print reqList1     
    print reqList2
                                                         
compare(newPlan,domainList)

