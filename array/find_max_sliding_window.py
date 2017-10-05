from collections import deque

def find_max_sliding_window(array, window_size):
    if window_size > len(array):
        return

    window = deque()

    # for i in xrange(0, window_size):
    #     while window and array[i] >= array[window[-1]]:
    #         window.pop()
    #     window.append(i)

    # print array[window[0]]

    for i in xrange(0, len(array)):
        while window and array[i] >= array[window[-1]]:
            window.pop()
        if window and (window[0] <= i - window_size):
            window.popleft()

        window.append(i)

        print array[window[0]]

def main():
    array = input("Enter array: ")
    key = input("Enter window size: ")
    print(find_max_sliding_window(array, key))

main()