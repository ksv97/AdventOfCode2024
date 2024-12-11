from linked_list import  LinkedList, Node
from time import  time

stones = LinkedList()

def apply_rules():
    current = stones.head
    while current is not None:
        if current.data == 0:
            current.data = 1
        elif len(str(current.data)) % 2 == 0:
            str_stone = str(current.data)
            middle = len(str_stone) // 2
            part1 = int(str_stone[:middle])
            part2 = int(str_stone[-middle:])
            current.data = part2
            stones.insert(current, part1)
        else:
            current.data *= 2024
        current = current.next

for x in open('task11_input.txt').readline().split():
    stones.append(int(x))

start = time()
for i in range(50):
    apply_rules()
    #stones.print()
print(stones.quantity)
print(time() - start)
