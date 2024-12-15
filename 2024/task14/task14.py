import re
from distutils.dir_util import create_tree
from sys import set_coroutine_origin_tracking_depth

width = 101
height = 103
#width = 11
#height = 7
seconds = 100
quadrants = [0,0,0,0]

all_unique_robots_positions = []

# 0 - 52 included
def get_tree_coords(startY):
    tree_robots = {}
    startX = width// 2
    tree_robots[(startX, startY)] = 0
    dx = 1
    dy = 1
    while startX + dx < width and startY + dy < height:
        for x in range(startX - dx, startX + dx + 1):
            tree_robots[(x, startY + dy)] = 0
        dx += 1
        dy += 1
    return tree_robots

def print_tree(robots_positions, file):
    for y in range(height):
        for x in range(width):
            if (x, y) in robots_positions:
                file.write('.')
            else:
                file.write(' ')
        file.write('\n')


def reset_tree(tree_robots):
    for key in tree_robots:
        tree_robots[key] = 0

def move_robot(startX, startY, dx, dy, seconds):
    newx = (startX + dx * seconds)
    newy = (startY + dy * seconds)
    finalY = newy % height if newy >= 0 else height - abs(newy) % height
    finalX = newx % width if newx >= 0 else width - abs(newx) % width
    if finalY == height: finalY = 0
    if finalX == width: finalX = 0
    return (finalX, finalY)

def update_quadrants_quantity(x, y):
    if x < width//2 and y < height // 2:
        quadrants[0] += 1
    elif x > width // 2 and y < height // 2:
        quadrants[1] += 1
    elif x < width // 2 and y > height // 2:
        quadrants[2] += 1
    elif x > width // 2 and y > height // 2:
        quadrants[3] += 1

def parse_input_line(line):
    pattern = r'-?\d+'
    point_str,velocity_str = line.split()
    x,y = map(int, re.findall(pattern, point_str))
    dx, dy = map(int, re.findall(pattern, velocity_str))
    return (x, y, dx, dy)

def solve1():
    for line in open('task14_input'):
        x, y, dx, dy = parse_input_line(line)
        #print(x,y,dx, dy)
        newx, newy = move_robot(x, y, dx, dy, seconds)
        print(newx, newy)
        update_quadrants_quantity(newx,newy)
    print(quadrants)
    result = 1
    for k in quadrants:
        result *= k
    print(result)


def solve2():
    robots = []
    for line in open('task14_input'):
        x, y, dx, dy = parse_input_line(line)
        #print(x,y,dx, dy)
        robots.append((x,y,dx,dy))

    seconds = 0
    f = open('result.txt', "w")
    while True:
        robots_positions = set()
        for (x,y,dx,dy) in robots:
            newx, newy = move_robot(x, y, dx, dy, seconds)
            robots_positions.add((newx, newy))

        f.write(str(seconds) + '\n')
        print_tree(robots_positions, f)
        #all_unique_robots_positions.append((seconds, robots_positions))
        # for startY in range(53): # experimentally discovered
        #     tree = get_tree_coords(startY)
        #     if is_robots_forming_tree(tree):
        #         print(seconds)
        #         break
        seconds += 1
        #print(seconds)
        #print('-----')
        if seconds == 100001:
            print('Done generating positions')
            break

    #print('Done creating file')

# get_tree_coords()
# print_tree()
# test_file=  open('task14_2_test', "w")
# for (x,y) in tree_robots:
#     test_file.write(f'p={x},{y} v=0,0\n')

solve2()
#solve1()