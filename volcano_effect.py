import sys

if __name__ == "__main__":
    n = int(raw_input().strip())
    m = int(raw_input().strip())
    maxEffect = 0
    d = {(i,j):0 for i in range(n) for j in range(n)}
    for a0 in xrange(m):
        x, y, w = raw_input().strip().split(' ')
        x, y, w = [int(x), int(y), int(w)]
        # Write Your Code Here
        startX, startY = x-w-1, y-w-1
        if startX < 0:
            startX = 0
        if startY < 0:
            startY = 0
        endX, endY = x+w-1, y+w-1
    
        if endX >= n:
            endX = n-1
        if endY >= n:
            endY = n-1
        
        print "startX ",startX," startY ", startY
        print "endX ",endX," endY ", endY
        
        for i in range(startX, endX+1):
            for j in range(startY, endY+1):
                d[(i,j)] += min(w-abs(x-i), w-abs(y-j))
                print i,j,d[(i,j)]
                if d[(i,j)] > maxEffect:
                    maxEffect = d[(i,j)]
    print maxEffect