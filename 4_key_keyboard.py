import numpy as np
import matplotlib.pyplot as plt

class Solution(object):
    def printA(self, N):
        #print N
        max = N
        if N<=6:
            self.d[N] = N
            return N
        else:
            for i in range(N-3,2,-1):
                if self.d[i]!=-1:
                    curr = self.d[i]*(N-i-1)
                else:
                    curr = self.printA(i)*(N-i-1)
                    #print self.d
                if curr>max:
                    max = curr
        self.d[N] = max
        return max

    def maxA(self, N):
        self.d = {i:-1 for i in xrange(N+1)}
        return self.printA(N)

def baseSolution(n):
    val = 1
    n-=1
    val_list_base.append(val)
    i=1
    while(n>0):
        if i%3==0:
            val=val*2
        val_list_base.append(val)
        n-=1
        i+=1

    return val_list_base


val_list_base = []
baseSolution(500)
val_list_original = []
s = Solution()
for i in range(500):
    val_list_original.append(s.maxA(i))


print val_list_base[-1],val_list_original[-1]
t = [i in range(1,501)]

plt.plot(t,val_list_base,'r') # plotting t,a separately 
plt.plot(t,val_list_original,'b') # plotting t,b separately 
plt.show()



