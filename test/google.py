# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

maxPathLength = 0

class Node:
    def __init__(self,id,label):
        self.id = id
        self.label = label
        self.children = []


def findLongestPath(root, nodeMap):
    print root.id
    global maxPathLength
    if len(root.children) == 0:
        return (root.label, 0)
    else:
        result = []
        for child in root.children:
            node = nodeMap[child]
            result.append(findLongestPath(node, nodeMap))

        result = sorted(result, key = lambda tup:tup[1], reverse=True)
        print root.id, result
        for r in result:
            if r[1] > maxPathLength:
                maxPathLength = r[1]
                
            if r[0] == root.label:
                if r[1]+1 > maxPathLength:
                    maxPathLength = r[1]+1
                return (root.label , r[1]+1)

        return (root.label, 0)


        
    
def solution(A, E):
    # write your code in Python 2.7
    global maxPathLength
    nodeMap = {}
    for i,label in enumerate(A):
        nodeMap[i+1] = Node(i+1, label)
    
    for j in range(len(A)-1):
        nodeMap[E[2*j]].children.append(E[2*j+1])
    
    findLongestPath(nodeMap[1], nodeMap)
    
    return maxPathLength
    

A = [1, 1, 1, 2, 2]
E = [1, 2, 1, 3, 2, 4, 2, 5]

print solution(A,E)

