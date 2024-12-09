import time
already_moved_blocks = dict()

def create_disk_map(input_line):
    disk_map = []
    file_number = 0
    for i in range(0, len(input_line), 2):
        disk_map.extend([str(file_number) for _ in range(int(input_line[i]))])
        file_number += 1
        if i + 1 < len(input_line):
            disk_map += '.' * int(input_line[i + 1])
    return disk_map

def find_right_block(disk_map, right_bound):
    current = right_bound - 1
    while current > 0 and disk_map[right_bound] == disk_map[current]:
        current -= 1
    return (current +1, right_bound)

def find_leftmost_insertion_position(disk_map, block_length):
    dots_count = 0
    dot_block_start = -1
    for i in range(len(disk_map)):
        if disk_map[i] =='.':
            dots_count += 1
            if dots_count == 1:
                dot_block_start = i
        else:
            if dots_count >= block_length:
                return dot_block_start
            dot_block_start = -1
            dots_count = 0
    return -1

def move_block(disk_map, block_start, block_end, insertion_start):
    insertion_position = insertion_start
    block_position = block_start
    while block_position <= block_end:
        disk_map[insertion_position] = disk_map[block_position]
        disk_map[block_position] = '.'
        block_position += 1
        insertion_position += 1

def rearrange_disk_map(disk_map):
    right = len(disk_map) - 1

    while right > 0:
        if disk_map[right] != '.':
            if disk_map[right] in already_moved_blocks:
                right -= already_moved_blocks[disk_map[right]]
                continue

            block_start, block_end = find_right_block(disk_map, right)
            block_length = block_end - block_start + 1
            right -= block_length
            #print(f'found block {block_start} {block_end} with the number {disk_map[block_start]}')
            insertion_position_start = find_leftmost_insertion_position(disk_map, block_length)
            if insertion_position_start == -1 or insertion_position_start >= block_start:
                # Если не найдена позиция вставки, двигаем к следующему блоку
                continue
            #print(f'found insertion position: {insertion_position_start} to {insertion_position_start + block_length}')
            already_moved_blocks[disk_map[block_start]] = block_length
            move_block(disk_map, block_start, block_end, insertion_position_start)
            #print(f'map after moving:')
            #print(*disk_map)
        else:
            right -= 1


def get_check_sum(disk_map):
    s = 0
    for i in range(len(disk_map)):
        if disk_map[i] == '.': continue

        s += int(disk_map[i]) * i
    return s

with open('task9_input.txt') as f:
    input_line = f.readline()


time1 = time.time()
disk_map = create_disk_map(input_line)
rearrange_disk_map(disk_map)
print(get_check_sum(disk_map))
print(time.time() - time1)