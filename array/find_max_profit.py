# def find_max_profit(array):
#     min_price = array[0]
#     max_profit = 0
#     for current_price in array:
#         min_price = min(min_price, current_price)
#         potential_profit = current_price - min_price
#         max_profit = max(potential_profit, max_profit)
#     return max_profit

def find_max_profit(array):
    if len(array) < 2:
        return
    min_price = array[0]
    max_profit = array[1] - array[0]
    for current_price in array[1:]:
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)
    return max_profit

def main():
    array = input("Enter array: ")
    print(find_max_profit(array))

main()