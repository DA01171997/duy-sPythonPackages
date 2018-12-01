#This merge_sort function
#is decreased by half
#This implementation has 
#complexity of O(n log(n)) 
#by Master Theroem

def merge_sort(V):
    n = len(V)
    #base case if len is 0 or 1 return V
    if n <= 1:
        return V
    #decrease by half base
    else:
        half = n // 2
        L = V[0:half]
        R = V[half:n]
        return merge(merge_sort(L), merge_sort(R))

#merge left and right in order
def merge(L, R):
    mergeList = list()
    li = ri = 0
    while li < len(L) or ri < len(R):
        if li == len(L):
            mergeList.append(R[ri])
            ri +=1
        elif ri == len(R):
            mergeList.append(L[li])
            li +=1
        elif L[li] <= R[ri]:
            mergeList.append(L[li])
            li += 1
        elif R[ri]<= L[li]:
            mergeList.append(R[ri])
            ri += 1
    return mergeList
