main_map = []
already_visited_map = []
region_perimeter = 0
region_area = 0

def can_go(x1, y1, x2, y2):
    return 0 <= x2 < len(main_map) \
    and 0 <= y2 < len(main_map[0])

def find_perimeter_and_area_for_region(x, y):
    global region_area
    global region_perimeter

    already_visited_map[x][y] = 1
    region_area += 1
    if x == 0: region_perimeter += 1
    if x == len(main_map) - 1: region_perimeter += 1
    if y == 0: region_perimeter += 1
    if y == len(main_map[0]) - 1: region_perimeter += 1

    directions = [(-1, 0), (1,0), (0, 1), (0,-1)]
    for dx, dy in directions:
        newx = x + dx
        newy = y + dy
        if can_go(x, y, newx, newy):
            # если клетка другого типа, увеличиваем периметр.
            if main_map[newx][newy] != main_map[x][y]:
                region_perimeter += 1
            # если того же, но мы еще туда не ходили,
            # продолжаем рекурсивный поиск от нее
            elif already_visited_map[newx][newy] == 0:
                find_perimeter_and_area_for_region(newx, newy)

def get_total_cost():
    total = 0
    global region_area
    global region_perimeter
    for x in range(len(main_map)):
        for y in range(len(main_map[0])):
            if already_visited_map[x][y] == 0:
                region_perimeter = 0
                region_area = 0
                find_perimeter_and_area_for_region(x,y)
                cost = region_perimeter * region_area
                total += cost
                print(f'region with the letter {main_map[x][y]} has the area of {region_area} and perimeter of {region_perimeter}')
    return total

with open('task12_input.txt') as f:
    for line in f:
        main_map.append(line.strip())
        already_visited_map.append([0 for i in range(len(line.strip()))])

print(get_total_cost())