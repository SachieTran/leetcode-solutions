S = [-5,-4,-3,-2,-1,0,0,1,2,3,4,5]

target = 0
S.sort()
resultSet = []
target = 0
listLength = len(S)
targetListLength = 4
for i,element in enumerate(S):
    print resultSet
    if len(resultSet) == 0:
        if (listLength-i >= targetListLength):
            resultSet.append((element,))
    else:
        set_length = len(resultSet)
        for j in xrange(set_length):
            currentList = list(resultSet[j])
            if len(currentList)<4:
                if (sum(currentList)+element) <= target:
                    resultSet.append(tuple(list(resultSet[j])+[element]))
        if (listLength-i >= targetListLength):
            resultSet.append((element,))

finalSet = set()
for l in resultSet:
    if len(l)==4 and sum(l)==0:
        finalSet.add(l)
print [list(i) for i in finalSet]


                