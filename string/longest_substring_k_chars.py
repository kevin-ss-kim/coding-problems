'''
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''

def longest_substring_k_chars(s, k):
    chars = dict()
    start, end, length, windowStart = 0, 0, 0, 0
    # function to count distinct number of characters
    countChar = lambda: sum(1 if x in chars and y > 0 else 0 for x, y in chars.items())
    for i in xrange(len(s)):
        # add into dictionary
        if i in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1
        end += 1
        # satisfy the k distinct characters
        while countChar() > k:
            chars[s[start]] -= 1
            start += 1
        # update the max length
        if end - start > length:
            length = end - start
            windowStart = start
    return s[windowStart:(windowStart + length)]

def longest_substring_k_chars_2(s, k):
    max_len, min_index, seen = 0, 0, {}
    for i in range(len(s)):
        seen[s[i]] = i
        if len(seen) > k:
            min_index = min(seen.values())
            del seen[s[min_index]]
            min_index += 1
        max_len = max(max_len, i - min_index + 1)
    return max_len

if __name__ == '__main__':
    s = input("Enter a string: ")
    k = input("Enter k: ")
    print(longest_substring_k_chars(s, k))