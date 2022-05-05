import sys
_ = list()
for i in range(int(input())):
    _.append(sys.stdin.readline().strip())
score = 0
sizuma = 0
for x in _:
    for y in range(len(x)):
        if x[y] == "O":
            score += 1
            sizuma += score
        else:
            score = 0
    print(sizuma)
    sizuma = 0
    score = 0