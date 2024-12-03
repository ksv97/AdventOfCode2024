import re

enabled = True

def get_sum_from_matches(matches):
    sum = 0
    numbers_pattern = r"\d{1,3}"
    for mul in matches:
        a, b = map(int, re.findall(numbers_pattern, mul))
        sum += a * b
    return sum

def process_line(line):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    sum = 0
    global enabled
    for i in range(len(line)):
        if line[i] == 'd':
            instruction = line[i:i+4]
            if instruction == 'do()':
                enabled = True
            else:
                instruction = line[i:i+7]
                if instruction == "don't()":
                    enabled = False
        elif line[i] == 'm':
            instruction = line[i:i+4]
            if instruction == 'mul(':
                matches = re.findall(pattern, line[i:i+12])
                if len(matches) > 0 and enabled:
                    sum += get_sum_from_matches(matches)
    return sum




# Тестовая строка
test_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

result = 0
for string in open('task3.txt'):
    result += process_line(string)
print(result)



# sum = 0
# for string in open('task3.txt'):
#
#     # Поиск совпадений
#     matches = re.findall(pattern, string)
#
#     numbers_pattern = r"\d{1,3}"
#     try:
#         for mul in matches:
#             a,b = map(int, re.findall(numbers_pattern, mul))
#             sum += a*b
#     except Exception as e:
#         print(e)
# print(sum)
