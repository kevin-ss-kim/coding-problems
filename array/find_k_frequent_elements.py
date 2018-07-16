def find_top_k_frequent_element(nums, k):
    elementToIndex = dict()
    indexToElement = dict()
    currentIndex = 0
    for value in nums:
        if value in elementToIndex:
            print(str(value) + " already found")
            nums[elementToIndex[value]] += 1
            # Bubble up and update index
            bubbleUpIndex = elementToIndex[value]
            parentIndex = (bubbleUpIndex - 1) / 2
            while (parentIndex >= 0) and (nums[bubbleUpIndex] > nums[parentIndex]):
                print("bubbling up index from " + str(bubbleUpIndex) + " to parent index " + str(parentIndex))
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
            print(str(value) + " not found, inserting")
            nums[currentIndex] = 1
            indexToElement[currentIndex] = value
            elementToIndex[value] = currentIndex
            currentIndex += 1
        print(nums[:currentIndex])
        print(indexToElement)
    a = []
    while k > 0:
        # remove element, then bubble down
        a.append(indexToElement[0])
        nums[0] = nums[currentIndex]
        currentIndex -= 1
        topIndex = 0
        checkIndex = nums[1] > num[2] then 1 else 2
    return a

def main():
    array = input("Enter sorted array: ")
    k = input("Enter k: ")
    print(find_top_k_frequent_element(array, k))

main()