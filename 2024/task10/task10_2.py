result = 0
main_map = []

def can_go(x1, y1, x2, y2):
    # can go, if it's not yet visited, is in map's bounds
    # and has the difference with previous point of 1
    return  0 <= x2 < len(main_map) \
            and 0 <= y2 < len(main_map[0]) \
            and main_map[x2][y2] - main_map[x1][y1] == 1

def find_all_trails(x, y):
    global result

    if main_map[x][y] == 9:
        result += 1
        return

    if can_go(x, y, x+1, y):
        find_all_trails(x+1, y)
    if can_go(x, y, x-1, y):
        find_all_trails(x - 1, y)
    if can_go(x, y, x, y+1):
        find_all_trails(x, y+1)
    if can_go(x, y, x, y-1):
        find_all_trails(x, y - 1)

def run1():
    with open('task10_input.txt') as f:
        for line in f:
            main_map.append([int(x) if x.isdigit() else -1 for x in line.strip()])

    for i in range(len(main_map)):
        for j in range(len(main_map[0])):
            if main_map[i][j] == 0:
                find_all_trails(i,j)

    print(result)

run1()