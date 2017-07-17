S = [1, 0, -1, 0, -2, 2]
S.sort()
resultSet = []
target = 0
listLength = len(S)
targetListLength = 4
for i,element in enumerate(S):
    if len(resultSet) == 0:
        if element<=target:
            resultSet.append((element,))
    else:
        set_length = len(resultSet)
        for i in xrange(set_length):
            currentList = list(resultSet[i])
            if len(currentList)<4:
                if (sum(currentList)+element) <= target:
                    resultSet.append(tuple(list(resultSet[i])+[element]))
        if (listLength-i >= targetListLength) and (element<=target):
            resultSet.append((element,))

finalSet = set()
for l in resultSet:
    if len(l)==4 and sum(l)==0:
        finalSet.add(l)
print [list(i) for i in finalSet]