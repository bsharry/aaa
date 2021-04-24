import random
def qsort(L):
  if len(L) <= 1:
    return
  p = L[0]
  low = 0
  high = len(L) - 1
  while low < high:
    while low < high and p < L[high]:
        high -= 1
    L[low] = L[high]
    while low < high and p > L[low]:
        low += 1
    L[high] =L[low]
  L[low] = p

  qsort(L[:low+1])
  qsort(L[low+1:])

b= [1,2,3,4,5,6,7,8,10]


random.shuffle(b)

print(b)

qsort(b)

print(b)



