def reorder_numbers(numbers):
    (swap_index1, swap_index2) = does_satisfy_all_rules(numbers)
    while (swap_index1, swap_index2) != (-1,-1):
        numbers[swap_index1], numbers[swap_index2] = numbers[swap_index2], numbers[swap_index1]
        (swap_index1, swap_index2) = does_satisfy_all_rules(numbers)

def does_satisfy_all_rules(numbers):
    for before,after in rules:
        if before not in numbers or after not in numbers: continue

        before_index = numbers.index(before)
        after_index = numbers.index(after)
        if before_index > after_index :
            return (before_index, after_index)
    return (-1,-1)

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
        if does_satisfy_all_rules(numbers) == (-1, -1): continue
        reorder_numbers(numbers)
        result += numbers[len(numbers) // 2]
print(result)
