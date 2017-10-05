def remove_duplicates(string):
    # O(n) runtime, O(n) memory
    hash_set = set()
    read_index = 0
    write_index = 0
    while read_index < len(string):
        if string[read_index] not in hash_set:
            hash_set.add(string[read_index])
            string[write_index] = string[read_index]
            write_index += 1
        read_index += 1
    return "'" + ''.join(string[:write_index]) + "'"

def remove_duplicates2(string):
    # O(n squared) runtime, O(1) memory
    read_index = 0
    write_index = 0
    while read_index < len(string):
        found = False
        for i in xrange(write_index):
            if string[i] == string[read_index]:
                found = True
                break
        if found == False:
            string[write_index] = string[read_index]
            write_index += 1
        read_index += 1
    return "'" + ''.join(string[:write_index]) + "'"

if __name__ == '__main__':
    string = input("Enter a string: ")
    print(remove_duplicates(list(string)))