import os
import copy
from compare import newPlan
from pyg import G
from input2 import domainList
from input2 import beliefs
from input2 import target
from input2 import planMetric
def plan(Pcur,DG,D,I,G,M):
    
    for i in range(len(Pcur)) :
        print "s",Pcur[i]
    for i in range(len(D)) :
        for j in range(len(D[i])) :
             print "D" , D[i][j]
    for i in range(len(I)) :
        print "B",I[i]
    for i in range(len(G)) :
        print "g", G[i]
    for i in range(len(M)) :
        print "P",M[i]
    dom = []
    for i in range(len(Pcur)) :
       for j in range(len(D)) :
            for k in range(len(D[j])) :
                       if(Pcur[i]==D[j][k]) :
                           if(Pcur[i+1]==D[j][k+1]) :
                             if(k==0) :
                                dom.append(D[j][k])
                                dom.append(D[j][k+1])
    print "dom",dom
    dom1 = []
    for j in range(len(D)):
       if(dom[len(dom)-2]==D[j][0]) :
                x = j
       elif(dom[len(dom)-4]==D[j][0]) :
                x = j
    dom1.append(D[j])
    print "dom1",dom1
    if(len(dom1) == 6) :
      for i in range(len(dom)) :  
        for j in range(len(D)) :
            for k in range(len(D[j])) :
                if(dom1[0][1]==D[j][3] and D[j][0]==dom[i]) :
                     dom1.append(D[j])
    print "dom1",dom1                             
    
plan(newPlan,G,domainList,beliefs,target,planMetric)  
