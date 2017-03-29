 
import sys
sys.path.append('..')
import pygraph
from pygraph.classes.Digraph import digraph
from pygraph.algorithms.critical import transitive_edges, critical_path
from pygraph.readwrite.dot import *
from compare import reqList1
from compare import reqList2
from shortestpath import *
#demo of the critical path algorithm and the transitivity detection algorithm
A = 'start:' + reqList1[0][1]
B = 'end:' + reqList1[0][1]
C = 'start:' + reqList2[0][0]
D = 'end:' + reqList2[0][0]


G = digraph()

G.add_node('Time 0')
G.add_node(A)
G.add_node(B)
G.add_node(C)
G.add_node(D)
#G.add_node('F')

G.add_edge('Time 0',A,d[0][1])
G.add_edge(A,'Time 0',d[1][0])
G.add_edge(A,B,reqList1[0][5])
G.add_edge(B,A,-1*(reqList1[0][4]))
G.add_edge(B,C,d[2][3])
G.add_edge(C,B,d[3][2])
G.add_edge(C,D,reqList2[0][5])
G.add_edge(D,C,-1*(reqList2[0][4]))
G.add_edge('Time 0',D,d[0][4])
G.add_edge(D,'Time 0',d[4][0])

print transitive_edges(G)
print critical_path(G)
print write(G,False)