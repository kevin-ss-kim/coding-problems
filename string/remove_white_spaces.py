def remove_white_spaces(string):
    # O(n) runtime, O(1) space
    read_index = 0
    write_index = 0
    while read_index < len(string):
        if string[read_index] != ' ':
            string[write_index] = string[read_index]
            write_index += 1
        read_index += 1
    return "'" + ''.join(string[:write_index]) + "'"

if __name__ == '__main__':
    string = input("Enter a string: ")
    print(remove_white_spaces(list(string)))