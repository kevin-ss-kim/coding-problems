'''
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

Example 1:

Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:

"<b>abc</b>xyz<b>123</b>"


Example 2:

Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]

Output:
"<b>aaabbc</b>c"

'''

def add_bold_tag(s, words):
    if len(words) == 0: return s
    interval = []
    for string in words:
        if string in words:
            index = 0
            
        index = s.find(string)
        if index > -1:
            interval.append((index, index + len(string)))
    boldString = ''
    # merge string
    if len(interval) == 0: return s
    interval = sorted(interval)
    merged_interval = [interval[0]]
    for start, end in interval:
        prev_start, prev_end = merged_interval[-1]
        if prev_end >= start:
            merged_interval[-1] = (prev_start, max(prev_end, end))
        else:
            merged_interval.append((start, end))
    index = 0
    for start, end in merged_interval:
        if index < start:
            boldString += s[index:start]
        boldString += '<b>' + s[start:end] + '</b>'
        index = end
    if index < len(s):
        boldString += s[index:]
    return boldString