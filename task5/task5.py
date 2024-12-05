def does_satisfy_all_rules(numbers):
    for before,after in rules:
        if before not in numbers or after not in numbers: continue

        if numbers.index(before) > numbers.index(after): return False
    return True

rules = []
result = 0
with open('task5_input.txt') as f:
    line = f.readline()
    while len(line) > 1:
        before,after = map(int,line.split('|'))
        rules.append((before,after))
        line = f.readline()

    for line in f:
        numbers = list(map(int, line.split(',')))
        if does_satisfy_all_rules(numbers):
            result += numbers[len(numbers) // 2]
print(result)
