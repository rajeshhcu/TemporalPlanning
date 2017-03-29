import copy
global d
from compare import *
from compare import *
d = []
d.append([])
d.append([])
d.append([])
d.append([])
d.append([])


#if(reqList1[0][5] == '150') :
#	a = 150
	
#if(reqList1[0][4] == '91') :
#	b = 91
	
#if(reqList2[0][4] == '150') :
	#c = 150
	
#if(reqList2[0][3] == '90') :
#	e = 90

f = 200
g = 0
	

	

d[0].append(0)
d[0].append(30)
d[0].append(100000)
d[0].append(100000)
d[0].append(f) 

d[1].append(-30)
d[1].append(0)
d[1].append(int(reqList1[0][5]))
d[1].append(100000)
d[1].append(100000)

d[2].append(100000)
d[2].append(-1*int(reqList1[0][4]))
d[2].append(0)
d[2].append(100000)
d[2].append(100000)

d[3].append(100000)
d[3].append(100000)
d[3].append(0)
d[3].append(0)
d[3].append(int(reqList2[0][4]))

d[4].append(g)
d[4].append(100000)
d[4].append(100000)
d[4].append(-1*int(reqList2[0][3]))
d[4].append(0)

global dist
dist = []
dist.append([])
dist.append([])
dist.append([])
dist.append([])
dist.append([])

dist[0].append(0)
dist[0].append(30)
dist[0].append(100000)
dist[0].append(100000)
dist[0].append(f) 

dist[1].append(-30)
dist[1].append(0)
dist[1].append(int(reqList1[0][5]))
dist[1].append(100000)
dist[1].append(100000)

dist[2].append(100000)
dist[2].append(-1*int(reqList1[0][4]))
dist[2].append(0)
dist[2].append(100000)
dist[2].append(100000)

dist[3].append(100000)
dist[3].append(100000)
dist[3].append(0)
dist[3].append(0)
dist[3].append(int(reqList2[0][4]))


dist[4].append(g)
dist[4].append(100000)
dist[4].append(100000)
dist[4].append(-1*int(reqList2[0][3]))
dist[4].append(0)

print "d",d
 
