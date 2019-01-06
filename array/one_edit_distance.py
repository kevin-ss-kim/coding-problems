'''
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
'''

def isOneEditDistancesd(s, t):
    diff = abs(len(s) - len(t))
    if diff > 1:
        return False
    if diff == 0:
        for i in range(len(s)):
            if s[i] != t[i]:
                return s[i+1:] == t[i+1:]
        return False
    else:
        # diff = 1
        if len(s) < len(t): smallerString, largerString = s, t
        else: smallerString, largerString = t, s
        for i in range(len(smallerString)):
            if smallerString[i] != largerString[i]:
                return smallerString[i:] == largerString[i+1:]
        return True