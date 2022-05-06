x=int(input());y=int(input());_=[0]
for n in range(x,y+1):
    err = 0
    for i in range(2, n):
        if n % i == 0:err = 1
    if err != 1:_.append(n)
print(sum(_+"\n"+_[1])) if len(_)>1 else print("-1")