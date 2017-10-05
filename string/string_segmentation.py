def string_segmentation(words, target, solved):
    # O(n squared) runtime(memoization), O(n) memory(depth of recursion tree)
    for i in xrange(len(target) + 1):
        first_word = target[0:i]
        second_word = target[i:]
        if first_word in words:
            if second_word == '' or second_word in words:
                return True
            if second_word not in solved:
                if string_segmentation(words, second_word, solved):
                    return True
                solved.add(second_word)
    return False

if __name__ == '__main__':
    string = input("Enter strings: ")
    target = input("Enter target string: ")

    print(string_segmentation(list(string), target, set()))