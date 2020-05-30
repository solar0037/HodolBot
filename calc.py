import math


def circle_circumference(r):
    return 2 * math.pi * r


def circle_area(r):
    return math.pi * r * r


def prob_to_code(message):
    prob = message[11:]
    code = ""
    cnt = 0

    while 1:
        if cnt == len(prob):
            break
        if prob[cnt] == '+':
            code += '%2B'
        elif prob[cnt] == '-':
            code += '-'
        elif prob[cnt] == '*':
            code += '*'
        elif prob[cnt] == '/':
            code += '%2F'
        elif prob[cnt] == '^':
            code += '%5E'
        elif prob[cnt] == '(':
            code += '%28'
        elif prob[cnt] == ')':
            code += '%29'
        elif prob[cnt] == '=':
            code += '%3D'
        else:
            code += prob[cnt]
        cnt += 1

    print(code)
    return code
