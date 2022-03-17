import pandas as pd
import random


def blue_eyes_one():
    all_fans = pd.read_csv("../data/comments-test.csv", sep="\t")
    lottery_pool = set()
    for index, row in all_fans.iterrows():
        lottery_pool.add(row['name'])
    list_all = list(lottery_pool)
    print("#############################################################")
    print("青眼白龙卡套获奖名单如下：\n")
    for i in range(3):
        blue_eyes = (random.choice(list_all))
        list_all.remove(blue_eyes)
        print("第{0}名获奖粉丝: ".format(i+1), blue_eyes)

    print("#############################################################")

    print("黑魔导女孩套装获奖名单如下：\n")
    for i in range(1):
        blue_eyes = (random.choice(list_all))
        list_all.remove(blue_eyes)
        print("第{0}名获奖粉丝: ".format(i+1), blue_eyes)
    print("#############################################################")

def main():
    blue_eyes_one()


if __name__ == '__main__':
    main()

