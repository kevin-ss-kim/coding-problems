def create_permutations(string):
    if len(string) < 2:
        return set([string])
    last_char = string[-1]
    string_except_last_char = string[:-1]
    permutations_except_last_char = create_permutations(string_except_last_char)
    permutations = set()
    for permutation_except_last_char in permutations_except_last_char:
        for position in range(len(string_except_last_char) + 1):
            permutation = (permutation_except_last_char[:position] + last_char + permutation_except_last_char[position:])
            permutations.add(permutation)
    return permutations

if __name__ == '__main__':
    string = input("Enter a string: ")
    print(create_permutations(string))