'''
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''

def longest_substring_k_chars(s, k):
    chars = set()
    start, end, n = 0, 0, 0
    while n < len(s):
        if s[end] not in chars and len(chars) == k:
            chars.remove(s[start])
            start += 1
        else:
            chars.add(s[end])
            end += 1
        n += 1
    return s[start:end]

if __name__ == '__main__':
    s = input("Enter a string: ")
    k = input("Enter k: ")
    print(longest_substring_k_chars(s, k))