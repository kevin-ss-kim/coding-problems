from collections import deque

def has_valid_parentheses(s):
    """
    :type s: str
    :rtype: bool
    """
    matching = {'[' : ']', '(' : ')', '{' : '}'}
    queue = deque()
    for i in xrange(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            queue.append(s[i])
        elif s[i] == ')' or s[i] == ']' or s[i] == '}':
            element = queue.pop()
            if matching[element] != s[i]:
                return False
    return len(queue) == 0

if __name__ == '__main__':
    string = input("Enter a string: ")
    print(has_valid_parentheses(string))