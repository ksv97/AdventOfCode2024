# find out how many times number in first list appears in
# second list and then multiply by value of number 1.
# do it for each number in first list

a = dict()
b = []
with open('task1_input.txt') as f:
    for line in f:
        n1, n2 = map(int, line.split())
        if n1 not in a:
            a[n1] = 1
        else:
            a[n1] += 1
        b.append(n2)

result = 0
for key in a:
    counting = b.count(key)
    result += key*a[key]*counting
print(result)