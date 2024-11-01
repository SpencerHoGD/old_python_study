"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
每次下注10元
输光或者赢到1500元，就收手
看看可以玩多少场
Version: 0.1
Author: hxm
"""
from random import randint

money = 1000
debt = 10
count = 0
while money > 0 and money <= 1500:
    # print('你的总资产为:', money)
    needs_go_on = False
    # while True:
    #     debt = int(input('请下注: '))
    #     if 0 < debt <= money:
    #         break
    first = randint(1, 6) + randint(1, 6)
    # print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        # print('玩家胜!')
        money += debt
        count += 1
    elif first == 2 or first == 3 or first == 12:
        # print('庄家胜!')
        money -= debt
        count += 1
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        # print('玩家摇出了%d点' % current)
        if current == 7:
            # print('庄家胜')
            money -= debt
            count += 1
        elif current == first:
            # print('玩家胜')
            money += debt
            count += 1
        else:
            needs_go_on = True
# print('你破产了, 游戏结束!')
print(f'you played {count} times, now you have {money} dollar')