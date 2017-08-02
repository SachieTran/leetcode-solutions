def maxA(N):
    max = N
    if N<=6:
        return N
    else:
        for i in range(N-3,0,-1):
            curr = maxA(i)*(N-i-1)
            print i, curr
            if curr>max:
                max = curr

    return max

print maxA(11)

