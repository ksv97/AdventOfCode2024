# Find out the summary distance betweeen each pair of elements
# in two sorted lists

a = []
b = []
with open('task1_input.txt') as f:
    for line in f:
        n1, n2 = map(int, line.split())
        a.append(n1)
        b.append(n2)

a.sort()
b.sort()
sum_distance = 0
for i in range(len(a)):
    sum_distance += abs(a[i] - b[i])
print(sum_distance)