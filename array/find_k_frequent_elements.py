def find_top_k_frequent_element(nums, k):
    a = [None] * (len(nums) + 1)
    elementToIndex = dict()
    for value in nums:
        if value in elementToIndex:
            index = elementToIndex[value]
            a[index].remove(value)
            if a[index + 1] is None:
                a[index + 1] = [value]
            else:
                a[index + 1].append(value)
            elementToIndex[value] = index + 1
        else:
            if a[1] is None:
                a[1] = [value]
            else:
                a[1].append(value)
            elementToIndex[value] = 1
    returnList = []
    currIndex = len(nums)
    while k > 0:
        if a[currIndex] is None or a[currIndex] == []:
            currIndex -= 1
        else:
            returnList.append(a[currIndex].pop())
            k -= 1
    return returnList

def main():
    array = input("Enter sorted array: ")
    k = input("Enter k: ")
    print(find_top_k_frequent_element(array, k))

main()