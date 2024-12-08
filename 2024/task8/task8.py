main_map = []
answer = set()

def find_new_points(x1,y1,x2,y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if x1 < x2: # первая точка по иксу выше второй
        x3 = x1 - dx
        x4 = x2 + dx
    else: # первая точка по иксу ниже второй
        x3 = x1 + dx
        x4 = x2 - dx

    if y1 < y2: # первая точка по игреку левее второй
        y3 = y1 - dy
        y4 = y2 + dy
    else: # первая точка по игреку правее второй
        y3 = y1 + dy
        y4 = y2 - dy

    return (x3,y3,x4,y4)

def try_set_point(x,y):
    global answer
    if 0 <= x < len(main_map) and 0 <= y < len(main_map[0]):
        if (x,y) not in answer:
            answer.add((x,y))


def process_point_of_the_same_sign(x, y):
    sign = main_map[x][y]
    # Найти все следующие дальше точки
    for i in range(x, len(main_map)):
        start_column = y+1 if i == x else 0
        for j in range(start_column, len(main_map[0])):
            if main_map[i][j] == sign:
                print(f'found {x};{y} and {i};{j} as {sign}')
                x1,y1,x2,y2 = find_new_points(x,y, i, j)
                try_set_point(x1,y1)
                try_set_point(x2,y2)


with open('task8_input') as f:
    for line in f:
        line = line.strip()
        main_map.append([x for x in line])

def solve1():
    for x in range(len(main_map)):
        for y in range(len(main_map[0])):
            if main_map[x][y].isalnum():
                process_point_of_the_same_sign(x,y)

#print(find_new_points(2,5,3,7))

solve1()
for i in main_map:
    print(*i,sep='')
print(len(answer))
