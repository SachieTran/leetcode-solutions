def displayTable(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            print table[i][j],
        print ""

def budgetShopping(n, bundleQuantities, bundleCosts):
    table = [[0 for j in range(n+1)] for i in range(len(bundleCosts)+1)]
    for i in range(len(bundleCosts)+1):
        table[i][0] = 0
    for i in range(n+1):
        table[0][i] = 0
    
    for i in range(1,len(bundleCosts)+1):
        for j in range(n+1):
            if bundleCosts[i-1] > j:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(table[i-1][j], bundleQuantities[i-1]+table[i][j-bundleCosts[i-1]])
    displayTable(table)
    return table[-1][-1]
# N = 50
# q = [20,19]
# c = [24,20]
N = 4
q = [10]
c = [2]
print budgetShopping(N, q, c)