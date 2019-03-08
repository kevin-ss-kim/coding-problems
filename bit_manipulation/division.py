'''

Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.
'''

def division(x, y):
    solution = 0
    power = 32
    yPower = y << power
    while x >= y:
        while yPower > x:
            power -= 1
            yPower = yPower >> 1
        solution += 1 << yPower
        x -= yPower
    return solution