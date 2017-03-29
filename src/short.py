from ctypes import *
from shortestpath import * 


#class STRUCT(Structure) :
 #         _fields_ = [("u",c_int),
  #                   ("v",c_int),
   #                  ("w",c_int)]

 

#global edjes

#edjes = STRUCT()
#edjes = []

 
#def printDist(si,ei) :
       
 #      print "Distances:\n"
  #     print "ei",ei
   #    print "\n\n"
    #   return di[0][si][ei]
 
def bellman_ford() :
      di.append(d)  
      for si in range(0,n):    
         for k in range(0,n):
             for u in range(0,n):
	           if(u!=si):
		         for i in range(0,n):
		                 if(i!=u and i!=si) :
					if(di[0][si][u]>d[si][i]+d[i][u]) :
						di[0][si][u] = d[si][i]+d[i][u]
      print "di",di     
					

 
def short() :
    
    global e
    e = 0
    global n
    global di
    di = []
    
    #n = len(d)
    n = len(d[0])
    #w = []
    #for i in range(0,n):
    #    for j in range(0,n):
    #            w.append(d[i][j])
    	    
     #	        edjes.append(e)
	#	edjes[e] = STRUCT(i,j,w[e])
			
	#	e=e+1
		
   
    bellman_ford()   
    #return printDist()
short()
   


 
