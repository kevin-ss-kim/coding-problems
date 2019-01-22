'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    return addBinaryHelper(a, b, 0)

def addBinaryHelper(a, b, carry):
    if not a and not b:
        if carry: return "1"
        return ""
    elif not a:
        if carry and b[-1] == "1":
            return addBinaryHelper(a,b[:len(b)-1],1) + "0"
        return b[:len(b)-1] + str(carry + int(b[-1]))
    elif not b:
        if carry and a[-1] == "1":
            return addBinaryHelper(a[:len(a)-1],b,1) + "0"
        return a[:len(a)-1] + str(carry + int(a[-1]))
    else:
        p_sum = int(a[-1]) + int(b[-1]) + carry
        if p_sum > 1:
            carry = 1
            p_sum -= 2
        else:
            carry = 0
        return addBinaryHelper(a[:len(a)-1], b[:len(b)-1], carry) + str(p_sum)