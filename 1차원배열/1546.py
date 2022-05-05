x = int(input())
y = list(map(int, input().split()))
_ = list()
for i in range(x):
    _.append(y[i]/max(y)*100)
print(sum(_)/x)