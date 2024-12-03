# how many lines satisfies the following:
# all are decreasing or increasing
# minimum on 1 maximum on 3

answer = 0
with open('task2.txt') as f:
    for line in f:
        a = list(map(int, line.split()))
        increasing = 0
        decreasing = 0
        for i in range(len(a) - 1):
            diff = a[i+1] - a[i]
            if 1 <= abs(diff) <= 3:
                if diff < 0:
                    decreasing += 1
                else:
                    increasing += 1
        if increasing == len(a) - 1 or decreasing == len(a) - 1:
            answer += 1
print(answer)