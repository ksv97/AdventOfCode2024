main_map = []
robot_position = (0,0)
movements = ""

def print_map_state():
    for i in main_map:
        print(*i)
    print(robot_position)

def get_movement_direction(move_sign):
    movement_directions = {
        '^': (-1, 0),
        '>': (0, 1),
        '<': (0, -1),
        'v': (1, 0)
    }
    return movement_directions[move_sign]

def parse_input():
    global robot_position
    global movements
    with open('task15_input') as f:
        for line_map in f:
            if line_map.strip() == '':
                break
            main_map.append([x for x in line_map.strip()])
            robot_index = line_map.find('@')
            if robot_index >= 0:
                robot_position = (len(main_map) - 1, robot_index)

        movements = ''.join([line.strip() for line in f])

def find_boxes_chain_length(startx, starty, direction):
    k = 1
    newx, newy = startx + direction[0], starty + direction[1]
    while main_map[newx][newy] == 'O':
        k += 1
        newx, newy = newx + direction[0], newy + direction[1]
    return k

def try_move_boxes_chain(chain_startX, chain_startY, chain_length, direction):
    boxes_tailX, boxes_tailY = chain_startX + chain_length * direction[0], chain_startY + chain_length * direction[1]
    if main_map[boxes_tailX][boxes_tailY] == '#': return False

    currentX, currentY = boxes_tailX, boxes_tailY
    while currentX != chain_startX or currentY != chain_startY:
        main_map[currentX][currentY] = 'O'
        currentX -= direction[0]
        currentY -= direction[1]
    main_map[currentX][currentY] = '.'
    return True

def change_robot_position(newx, newy):
    global robot_position
    main_map[robot_position[0]][robot_position[1]] = '.'
    robot_position = (newx, newy)
    main_map[robot_position[0]][robot_position[1]] = '@'


def move(movement_sign):
    global robot_position
    direction = get_movement_direction(movement_sign)
    newx, newy = (robot_position[0] + direction[0], robot_position[1] + direction[1])
    if main_map[newx][newy] == '#': return
    if main_map[newx][newy] == '.':
        change_robot_position(newx, newy)
        return

    boxes_chain_length = find_boxes_chain_length(newx, newy, direction)
    if try_move_boxes_chain(newx, newy, boxes_chain_length, direction):
        change_robot_position(newx, newy)

def calculate_boxes_GPS():
    result = 0
    for x in range(len(main_map)):
        for y in range(len(main_map[0])):
            if main_map[x][y] == 'O':
                result += x * 100 + y
    return result
def solve1():

    parse_input()
    print_map_state()
    print(movements)
    for sign in movements:
        move(sign)
    print(calculate_boxes_GPS())

solve1()
