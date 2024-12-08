from itertools import product


def process_line(line, task_number=1):
    result, numbers = line.split(':')
    result = int(result)
    numbers = list(map(int, numbers.split()))
    # все возможные комбинации
    available_combs = [0,1] if task_number == 1 else [0,1,2]
    combs = product(available_combs, repeat=len(numbers)-1)
    for comb in combs:
        comb_result = get_result(comb, numbers)
        if comb_result == result:
            return result
    return 0

def get_result(comb, numbers):
    s = numbers[0]
    for i in range(len(comb)):
        if comb[i] == 0:
            s += numbers[i+1]
        elif comb[i] == 1:
            s *= numbers[i + 1]
        else:
            s = int(str(s) + str(numbers[i+1]))
    return s

answer = 0
with open('task7_input.txt') as f:
    for line in f:
        answer += process_line(line.strip(),2)
print(answer)
