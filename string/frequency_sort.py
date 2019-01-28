'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    charCount = {}
    for i in range(len(s)):
        charCount[s[i]] = charCount.get(s[i], 0) + 1
    charCount = sorted(charCount.items(), key=lambda x: x[1], reverse=True)
    string = ""
    for c, i in charCount:
        string += c * i
    return string