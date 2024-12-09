def create_disk_map(input_line):
    disk_map = []
    file_number = 0
    for i in range(0, len(input_line), 2):
        disk_map.extend([str(file_number) for _ in range(int(input_line[i]))])
        file_number += 1
        if i + 1 < len(input_line):
            disk_map += '.' * int(input_line[i + 1])
    return disk_map

def rearrange_disk_map(disk_map):
    position_to_move = len(disk_map) - 1
    insert_position = disk_map.index('.')
    while insert_position < position_to_move:
        while disk_map[insert_position] != '.':
            insert_position += 1

        while disk_map[position_to_move] == '.':
            position_to_move -= 1

        if insert_position < position_to_move:
            disk_map[insert_position] = disk_map[position_to_move]
            insert_position += 1
            disk_map[position_to_move] = '.'
            position_to_move -= 1

def get_check_sum(disk_map):
    s = 0
    for i in range(len(disk_map)):
        if disk_map[i] == '.': break

        s += int(disk_map[i]) * i
    return s

with open('task9_input.txt') as f:
    input_line = f.readline()



disk_map = create_disk_map(input_line)
rearrange_disk_map(disk_map)
print(get_check_sum(disk_map))