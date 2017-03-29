import copy
import os
os.remove('/home/rajesht/Desktop/TemporalPlanning1/src/test1')
file = open("test", "r") 
text = file.read() 
file.close() 
file = open("test1", "w") 
file.write(text)
file.close()
                
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


def parsePlanFile(fileName):
    print "parsePlanFile Function"
    f = open(fileName)
    f = f.read()
    f = f.replace('[','( ')
    f = f.replace(']',' )')
    f = f.split() 
    global plan
    plan = []
    for i in range(len(f)) :
           plan.append(parseBelief(f)[0])
	   
    return plan[0]
#parsePlanFile('C:\\Python26\\TemporalPlanning1\\src\\test1.txt')
	   

def parseDomainFile(fileName):
    print "parseDomainFile Function"
    f = open(fileName)
    domains = f.readlines()
    g = open(fileName)

    global actionList
    domainList = []
    for i in range(len(domains)):

        s = g.readline()
        s = s.split()
        domainList.append(parseBelief(s)[0])

    return domainList
#parseDomainFile('C:\\Python26\\TemporalPlanning1\\src\\planproject\\domain.txt')

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
#parseBeliefFile('./planproject/init')

def parsePlanMetricFile(filename) :
       print "parsePlanMetricFile function"
       f = open(filename)
       f = f.readline()
       f = f.split()
       planMetric = []
       planMetric.append(parseBelief(f))
       return planMetric
#parsePlanMetricFile('./planproject/planmetric')

def parseTargetFile(filename) :
       print "parseTargetFile"
       f = open(filename)
       f = f.readline()
       f = f.split()
       target = []
       target.append(parseBelief(f))
       return target
#parseTargetFile('./planproject/target')
         
def spacetest(filename) :
       f = open(filename)
       f = f.read()
       #os.remove('C:\\Python26\\TemporalPlanning1\\src\\test1.txt')
       os.remove('/home/rajesht/Desktop/TemporalPlanning1/src/test1')
       #fi = open('C:\\Python26\\TemporalPlanning1\\src\\test1.txt','a')   
       fi = open('/home/rajesht/Desktop/TemporalPlanning1/src/test1','a')   
       list = []
       
       for i in range(len(f)) :
               if (f[i]=='[') :
                        #list.append(f[i])
                         list.append(' ')
               elif (f[i]==',') :
                         list.append(' ')
                        #list.append(f[i])
                         list.append(' ')
               elif (f[i]==']') :
                         list.append(' ')
                        #list.append(f[i])
               else :
                         list.append(f[i])
       for j in range(len(list)) :                
              fi.write(list[j])
       fi.close()
                
          
#spacetest('C:\\Python26\\TemporalPlanning1\\src\\test.txt')



