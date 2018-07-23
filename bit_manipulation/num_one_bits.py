def num_one_bits(n):
    total = 0
    while n > 0:
        if n % 2 == 1: total += 1
        n = n / 2
    return total

if __name__ == '__main__':
    n = input("Enter number: ")
    print(num_one_bits(n))