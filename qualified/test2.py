# params: money, coins
# return: combinations
# description: count_change method takes the money-amount to change and the array of unique denominations as parameters and then returns the number of ways to change for a money-amount of this money

def count_change(money, coins):
    combinations = [0] * (money + 1) #create an array of size money-amount+1
    combinations[0] = 1 #number of combinations for money-amount 0
    for coin in coins:
        for iter in range(coin, money + 1):
            combinations[iter] += combinations[iter - coin]
    return combinations[money]


if __name__ == '__main__':
    print(count_change(4, [1, 2, 3]))