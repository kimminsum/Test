import sys
for i in range(int(input())):
    x = list(map(int, sys.stdin.readline().rstrip().split()))
    sizuma = 0
    for e in range(len(x)):
        if x[e] > (sum(x)-x[0])/x[0]: sizuma += 1
    print(f"{round((sizuma/x[0])*100, 3)}%")