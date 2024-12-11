def apply_rules():
    position = 0
    while position < len(stones):
        if stones[position] == 0:
            stones[position] = 1
        elif len(str(stones[position])) % 2 == 0:
            str_stone = str(stones[position])
            middle = len(str_stone) // 2
            stones[position] = int(str_stone[-middle:])
            stones.insert(position, int(str_stone[:middle]))
            position += 1
        else:
            stones[position] *= 2024
        position += 1

stones = []
for x in open('task11_input.txt').readline().split():
    stones.append(int(x))

for i in range(25):
    apply_rules()
print(stones)
print(len(stones))
