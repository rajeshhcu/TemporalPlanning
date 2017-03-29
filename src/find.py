import os
import copy
from shortestpath import *
from short import *
global newmin



def max(l) :
        if(l[0]>l[1]) :
	        return l[0]
	else:
		return l[1]
	
def absolute(ab,a,b) :
	if(a<0) :
		ab.append(-1*a)
		if(b<0) :
			ab.append(-1*b)
		else :
			ab.append(-1*b)
	else :
		ab.append(a)
		if(b<0) :
          		ab.append(-1*b)
		else :
			ab.append(b)	
	
	return ab

def lessthan(f,c,d) :
	if(c<d) :
		 newmin = 0
		 file = open(f, "r") 
                 text = file.read() 
                 file.close() 
	         for i in range(0,30):
		      newmin = newmin+c+1
		      file = open(f, "w") 
                      file.write(text.replace(str(-1*dist[2][1]),"".join("%s" % newmin)))
	      	      file.close()
		 
		
def overwrite():
	abs0 = []
	abs1 = []
        abs0 = copy.deepcopy(absolute(abs0,di[0][1][2],di[0][2][1]))
        abs1 = copy.deepcopy(absolute(abs1,di[0][3][4],di[0][4][3]))	       
        print "abs",abs0
	lessthan('./rpg/actionBase',max(abs0),dist[1][2])
	lessthan('./rpg/actionBase',max(abs1),dist[3][4])
		
overwrite()	
