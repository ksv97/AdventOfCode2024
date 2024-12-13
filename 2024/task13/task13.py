import re

class Equation:
    '''
    Equation of ax + by = c
    where x = numbers of btnA, y = numbers of btnB
    '''
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


def solve_equation_system(equation1: Equation, equation2: Equation):
    btnA = (equation2.c * equation1.b - equation2.b * equation1.c) / (equation2.a * equation1.b - equation2.b * equation1.a)
    btnB = (equation1.c - equation1.a * btnA) / equation1.b
    return (btnA, btnB)

# # Если решение не в целых числах, то NoSolution
# samples = [(Equation(94, 22, 8400), Equation(34, 67, 5400)),
#            (Equation(26, 67, 12748), Equation(66,21,12176)),
#            (Equation(17,84,7870), Equation(86,37,6450)),
#            (Equation(69,27,18641), Equation(23,71,10279))]
#
# for eq1, eq2 in samples:
#     print(solve_equation_system(eq1, eq2))
def parse_XY(patternX, patternY, line):
    matchedX = re.findall(patternX, line)
    matchedY = re.findall(patternY, line)
    pattern_number = r'\d+'
    X = re.findall(pattern_number, matchedX[0])
    Y = re.findall(pattern_number, matchedY[0])
    return int(X[0]), int(Y[0])

answer = 0
with open('task13_input.txt') as f:
    patternX = r"X\+\d+"
    patternY = r"Y\+\d+"
    pattern_prizeX = r"X\=\d+"
    pattern_prizeY = r"Y\=\d+"
    line_break = '.'
    while line_break != '':
        line_btnA = f.readline()
        line_btnB = f.readline()
        line_prize = f.readline()
        line_break = f.readline()
        (a1, a2) = parse_XY(patternX, patternY, line_btnA)
        (b1, b2) = parse_XY(patternX, patternY, line_btnB)
        (c1, c2) = parse_XY(pattern_prizeX, pattern_prizeY, line_prize)
        eq1 = Equation(a1,b1,c1)
        eq2 = Equation(a2,b2,c2)
        (btnA, btnB) = solve_equation_system(eq1, eq2)
        if int(btnA) != btnA or int(btnB) != btnB or btnA > 100 or btnB > 100:
            continue # no solution

        answer += btnA*3 + btnB
print(int(answer))

