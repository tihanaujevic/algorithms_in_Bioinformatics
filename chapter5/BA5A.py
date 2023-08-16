# Find the Minimum Number of Coins Needed to Make Change

def change (money, coins):
    mini = (money + 1) * [0]

    for i in range(1, money +1):
        mini[i] = i + 1
        for coin in coins:
            if i >= coin:
                if mini[i-coin] + 1 < mini[i]:
                    mini[i] = mini[i-coin] + 1
                
    return mini[money]

if __name__ == '__main__':
    import sys

    inlines = [x.strip('\n') for x in sys.stdin.readlines()]

    money = int(inlines[0])
    coins = [int(x) for x in inlines[1].split(',')]

    result = change (money, coins)

    sys.stdout.write(str(result))