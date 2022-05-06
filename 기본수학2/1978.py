from distutils.log import error
from math import erfc


n=int(input());_=list(map(int, input().split(" ")));sig=0
for i in range(n):
    er=0
    for e in range(2, _[i]):
        if _[i]%e==0:
            er+=1
    if er == 0 and _[i]!=1:
        sig+=1
print(sig)