'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
'''

def decode_ways(s):
    return decode(s, {})

# Make use of memoization
def decode(s, mem):
    if s == '':
        return 1
    # Cannot decode numbers starting with 0
    elif s[0] == '0':
        return 0
    elif len(s) < 2:
        return 1
    elif s in mem:
        return mem[s]
    elif int(s[0:2]) <= 26:
        mem[s] = decode(s[1:], mem) + decode(s[2:], mem)
        return mem[s]
    else:
        mem[s] = decode(s[1:], mem)
        return mem[s]

if __name__ == '__main__':
    n = input("Enter number to decode: ")
    print(decode_ways(str(n)))