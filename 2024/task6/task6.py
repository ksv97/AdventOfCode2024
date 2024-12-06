import copy

main_map = []
current_position = (0,0)
direction = (-1, 0) # moving up
result = 0

def try_move(map):
    new_position = (current_position[0] + direction[0], current_position[1] + direction[1])
    if not (0 <= new_position[0] < len(map) and 0 <= new_position[1] < len(map[0])):
        return "out of bounds"
    elif map[new_position[0]][new_position[1]] == '#':
        return "wall"
    else:
        return "ok"

def move():
    global current_position
    current_position = (current_position[0] + direction[0], current_position[1] + direction[1])

def rotate():
    global direction
    if direction == (-1, 0):
        direction = (0, 1)
    elif direction == (0,1):
        direction = (1,0)
    elif direction == (1,0):
        direction = (0, -1)
    elif direction == (0,-1):
        direction = (-1, 0)

with open('task6_input.txt') as f:
    for line in f:
        line = line.strip()
        startIndex = line.find("^")
        if startIndex > -1:
            current_position = (len(main_map), startIndex)
        main_map.append([x for x in line])
    # starting cell counts


def solve1():
    already_visited_map = [[0 for i in range(len(main_map[0]))] for j in range(len(main_map))]
    already_visited_map[current_position[0]][current_position[1]] = 1
    result = 1
    while try_move(main_map) != "out of bounds":
        if try_move(main_map) == "wall":
            rotate()
        else:
            move()
            if already_visited_map[current_position[0]][current_position[1]] == 0:
                result += 1
                already_visited_map[current_position[0]][current_position[1]] = 1

    print(result)

def solve2(start_position):
    global direction
    global current_position
    result = 0
    map_copy = [[x for x in line] for line in main_map]
    for i in range(len(main_map)):
        for j in range(len(main_map[0])):
            map_copy[i][j] = '#'

            direction = (-1, 0)
            current_position = (start_position[0], start_position[1])
            already_visited_directions_map = [[(0, 0) for _ in range(len(main_map[0]))] for _ in range(len(main_map))]
            already_visited_directions_map[current_position[0]][current_position[1]] = (direction[0], direction[1])
            # trying to find loopings with the new wall
            foundLoop = False
            while try_move(map_copy) != "out of bounds":
                if try_move(map_copy) == "wall":
                    rotate()
                else:
                    move()
                    if already_visited_directions_map[current_position[0]][current_position[1]] == (0,0):
                        already_visited_directions_map[current_position[0]][current_position[1]] = (direction[0], direction[1])
                    elif already_visited_directions_map[current_position[0]][current_position[1]] == (direction[0], direction[1]):
                        foundLoop = True
                        break
            if foundLoop:
                result += 1

            map_copy[i][j] = main_map[i][j] # возврат к исходному состоянию карты
    print(result)
solve2(current_position)

# Идея для второй части. Запоминать не только посещенную вершину, но и последнее направление стражника
# Когда приходим в точку с тем же самым направлением и уже посещенную - это будет бесконечный цикл.