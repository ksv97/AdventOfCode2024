from queue import  Queue
from PointWithDirection import  PointWithDirection

main_map = []
start_point = PointWithDirection(0, 0)
end_point = PointWithDirection(0, 0)
with open('task16_input.txt') as f:
    for line in f:
        main_map.append([x for x in line.strip()])

    for x in range(len(main_map)):
        for y in range(len(main_map[0])):
            if main_map[x][y] == 'S':
                start_point = PointWithDirection(x, y)
            elif main_map[x][y] == 'E':
                end_point = PointWithDirection(x, y)

def bfs():
    queue = Queue()
    queue.put(start_point)
    cost_so_far = {start_point: 0}
    came_from = {start_point: None}

    while not queue.empty():
        current_point = queue.get()

        #if main_map[current_point.x][current_point.y] == 'E': break

        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            new_point = PointWithDirection(current_point.x + dx, current_point.y + dy, (dx,dy))
            #print(f'checking point {new_point}')
            new_cost = current_point.get_cost(new_point) + cost_so_far[current_point]
            #print(f'cost is {new_cost}')
            if main_map[new_point.x][new_point.y] == '#': continue
            #print(f'cost so far:{None if new_point not in cost_so_far else cost_so_far[new_point]}')
            if new_point not in cost_so_far or new_cost < cost_so_far[new_point]:
                cost_so_far[new_point] = new_cost
                came_from[new_point] = current_point
                queue.put(new_point)
                #print(f'add point {new_point} to queue')
        #print(f'current map result after searching from {current_point}')
        #print_cost_map(cost_so_far)
        #print(f'queue state: ')
        #print(queue)

    # print_cost_map(cost_so_far)
    # current_point = PointWithDirection(end_point.x, end_point.y)
    # while came_from[current_point] is not None:
    #     print(current_point)
    #     current_point = came_from[current_point]


    return cost_so_far[end_point]

def print_cost_map(costs_so_far):
    for x in range(len(main_map)):
        for y in range(len(main_map[0])):
            point =PointWithDirection(x,y)
            if  point in costs_so_far:
                print(costs_so_far[point], end=' '*(6-len(str(costs_so_far[point]))))
            else:
                print('#',end = '     ')
        print()



def heuristic(next, goal):
    return abs(next.x - goal.x) + abs(next.y + goal.y)

print(bfs())