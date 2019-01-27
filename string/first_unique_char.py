'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''

def firstUniqueChar(s):
    firstOccurences = {}
    moreThanOne = set()
    for i in range(len(s)):
        if s[i] in firstOccurences:
            del firstOccurences[s[i]]
            moreThanOne.add(s[i])
        elif s[i] not in moreThanOne:
            firstOccurences[s[i]] = i
    if len(firstOccurences) == 0: return -1
    return min(firstOccurences.items(), key=(lambda x: x[1]))[1]