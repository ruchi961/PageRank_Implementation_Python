#Page Rank
#nodes= [“A”,”B”,”C”,”D”]
#graph of form {“A”:[[incoming edges],[#outgoing edges]]}
from random import randrange
graph={}
nodes=[]
no_vertices=int(input(“Please enter the number of vertices in the graph : “))
for I in range(no_vertices):
    print(“Vertex “,I,end=” : “)
    nodes.append(input())
for I in nodes:
    incoming=[]
    print(“”.center(80,”-“))
    print(“For vertex “,i)
    print(“”.center(80,”*”))
    incoming_edges = []
    outgoing_edges = []
    in_count=int(input(“Please enter the number of incoming edges :”))
    out_count = int(input(“Please enter the number of outgoing edges :”))
    print(“”.center(80,”*”))
    while in_count>0:
        val =input(“Please enter the incoming edges of Vertex : “)
        while True:
          
            if val not in nodes:
                print(“Please enter any node belonging to the graph.........”)
                val =input(“Please enter the incoming edges of Vertex : “)
            else:
                break
        incoming_edges.append(val)
        in_count = in_count – 1
    while out_count>0:
        val =input(“Please enter the outgoing edges of Vertex : “)
        while True:
        
            if val not in nodes:             
                print(“Please enter any node belonging to the graph.........”)
                val =input(“Please enter the outgoing edges of Vertex : “)
            else:
                break
        outgoing_edges.append(val)
        out_count = out_count – 1
    print(“”.center(80,”*”))
    graph[i]=[]
    graph[i].append(incoming_edges)
    graph[i].append(outgoing_edges)
print(graph)
#damping factor
d=0.85
pageRank={}
#initiliazing Pank rank to 1 initially
for I in nodes:
    pageRank[i] = 1
#randomly choose a starting node to begin with
PRDone=[]

for I in range(no_vertices):
    while True:
        nodePR = nodes[randrange(0,no_vertices)]
        if nodePR not in PRDone:
            PRDone.append(nodePR)
            break
    incomingNodes = graph[nodePR][0]
    val_sum=0
    for I in incomingNodes:
        val_sum = val_sum + pageRank[i]/len(graph[i][1])
    pageRank[nodePR] = (1-d) + (d*(val_sum))
    
print(“Page rank of the vertices is “,pageRank)
