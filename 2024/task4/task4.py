text = []
with open('task4_input.txt') as f:
    for line in f:
        text.append(line.strip())

result = 0
XMAS = 'XMAS'
for i in range(len(text)):
    for j in range(len(text[0])):
        if j < len(text[0]) - 3:
            left_to_right = text[i][j:j+4]
            if left_to_right == XMAS: result += 1
        if j >= 3:
            right_to_left = text[i][j-3:j+1][::-1]
            if right_to_left == XMAS: result += 1
        if i < len(text) - 3:
            top_to_bottom = ''.join([text[k][j] for k in range(i, i+4)])
            if top_to_bottom == XMAS: result += 1
        if i >= 3:
            bottom_to_top = ''.join([text[k][j] for k in range(i, i-4, -1)])
            if bottom_to_top == XMAS: result += 1
        if i < len(text) - 3 and j < len(text[0]) - 3:
            left_top_to_right_bottom =  ''.join([text[i+k][j+k] for k in range(4)])
            if left_top_to_right_bottom == XMAS: result += 1
        if i < len(text) - 3 and j >= 3:
            right_top_to_left_bottom = ''.join([text[i+k][j-k] for k in range(4)])
            if right_top_to_left_bottom == XMAS: result += 1
        if i >= 3 and j >= 3:
            right_bottom_to_left_top = ''.join([text[i-k][j-k] for k in range(4)])
            if right_bottom_to_left_top == XMAS: result += 1
        if i >= 3 and j < len(text[0]) - 3:
            left_bottom_to_right_top = ''.join([text[i-k][j+k] for k in range(4)])
            if left_bottom_to_right_top == XMAS: result += 1
print(result)

