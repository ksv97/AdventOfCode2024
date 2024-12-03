# how many lines satisfies the following:
# all are decreasing or increasing
# minimum on 1 maximum on 3
# AND maybe can delete one to make it good
from operator import index


def is_correct(numbers):
    # wether satisfy
    # all are decreasing or increasing
    # minimum on 1 maximum on 3
    increasing = 0
    decreasing = 0
    for i in range(len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if 1 <= abs(diff) <= 3:
            if diff < 0:
                decreasing += 1
            else:
                increasing += 1
    if increasing == len(numbers) - 1 or decreasing == len(numbers) - 1:
        return True
    return False

answer = 0
with open('task2.txt') as f:
    for line in f:
        a = list(map(int, line.split()))
        if is_correct(a):
            answer += 1
        else:
            for i in range(len(a)):
                numbers_copy = a.copy()
                numbers_copy.pop(i)
                if is_correct(numbers_copy):
                    answer += 1
                    break
print(answer)