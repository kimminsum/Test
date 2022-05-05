n=list(input())
for i in range(26):print(n.index(chr(97+i)),end=" ")if chr(97+i) in n else print(-1,end=" ")