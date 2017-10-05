def reverse_part(string, start, end):
    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1

def reverse_words(string):
    if len(string) < 2:
        return string
    reverse_part(string, 0, len(string) - 1)
    start = 0
    end = 0
    while True:
        while start < len(string) and string[start] == ' ':
            start += 1
        if start >= len(string):
            break
        end = start + 1
        while end < len(string) and string[end] != ' ':
            end += 1
        reverse_part(string, start, end - 1)
        start = end
    return '\'' + ''.join(string) + '\''

if __name__ == '__main__':
    string = input("Enter a sentence: ")
    print(reverse_words(list(string)))