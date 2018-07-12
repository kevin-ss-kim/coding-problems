def find_top_k_frequent_element(nums, k):
    elementToIndex = dict()
    indexToElement = dict()
    currentIndex = 0
    for index, value in enumerate(nums):
        if value in elementToIndex:
            nums[elementToIndex[value]] += 1
            # Bubble up and update index
            bubbleUpIndex = elementToIndex[value]
            parentIndex = (bubbleUpIndex - 1) / 2
            while (parentIndex >= 0) and (nums[bubbleUpIndex] >= nums[parentIndex]):
                # Bubble up and set dictionary
                childElement = indexToElement[bubbleUpIndex]
                parentElement = indexToElement[parentIndex]
                indexToElement[bubbleUpIndex] = parentElement
                indexToElement[parentIndex] = childElement
                elementToIndex[childElement] = nums[parentIndex]
                elementToIndex[parentElement] = nums[bubbleUpIndex]
                bubbleUpIndex = parentIndex
                parentIndex = (parentIndex - 1) / 2
        else:
            nums[currentIndex] = 1
            indexToElement[currentIndex] = value
            elementToIndex[value] = currentIndex
            currentIndex += 1
    a = []
    for i in xrange(k):
        a.append(indexToElement[i])
    return a

def main():
    array = input("Enter sorted array: ")
    k = input("Enter k: ")
    print(find_top_k_frequent_element(array, k))

main()