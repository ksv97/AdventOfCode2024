text = []
with open('task4_input.txt') as f:
    for line in f:
        text.append(line.strip())

result = 0
MAS = 'MAS'
for i in range(len(text)):
    for j in range(len(text[0])):
        if i < len(text) - 2 and j < len(text[0]) - 2:
            left_top_right_bottom = ''.join([text[i+k][j+k] for k in range(3)])

            if left_top_right_bottom == MAS:
                right_top_left_bottom = text[i][j+2] + text[i+1][j+1] +text[i+2][j]
                left_bottom_to_right_top = right_top_left_bottom[::-1]
                if right_top_left_bottom == MAS or left_bottom_to_right_top == MAS:
                    result += 1
        if i < len(text) - 2 and j >= 2:
            right_top_to_left_bottom = ''.join([text[i+k][j-k] for k in range(3)])
            if right_top_to_left_bottom == MAS:
                left_top_right_bottom = text[i][j-2] + text[i+1][j-1] +text[i+2][j]
                right_bottom_to_left_top = left_top_right_bottom[::-1]
                if left_top_right_bottom == MAS or right_bottom_to_left_top == MAS:
                    result += 1
        if i >= 2 and j < len(text[0]) - 2:
            left_bottom_to_right_top = ''.join([text[i-k][j+k] for k in range(3)])

            if left_bottom_to_right_top == MAS:

                left_top_right_bottom = text[i-2][j] + text[i-1][j+1] + text[i][j+2]
                right_bottom_left_top = left_top_right_bottom[::-1]
                if left_top_right_bottom == MAS or right_bottom_left_top == MAS:
                    result += 1
        if i >= 2 and j >= 2:
            right_bottom_to_left_top = ''.join([text[i - k][j - k] for k in range(3)])

            if right_bottom_to_left_top == MAS:

                left_bottom_to_right_top = text[i][j-2] + text[i-1][j-1] + text[i-2][j]
                right_top_to_left_bottom = left_bottom_to_right_top[::-1]
                if left_bottom_to_right_top == MAS or right_top_to_left_bottom == MAS:
                    result += 1
print(result // 2)


