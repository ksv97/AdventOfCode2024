import re

# Регулярное выражение
pattern = r"mul\(\d{1,3},\d{1,3}\)"

# Тестовая строка
#test_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
sum = 0
for string in open('task3.txt'):

    # Поиск совпадений
    matches = re.findall(pattern, string)

    numbers_pattern = r"\d{1,3}"
    try:
        for mul in matches:
            a,b = map(int, re.findall(numbers_pattern, mul))
            sum += a*b
    except Exception as e:
        print(e)
print(sum)
