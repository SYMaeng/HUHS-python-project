from random import *

ID = range(1,21)
ID = list(ID)
shuffle(ID)
get_prize = sample(ID, 4)
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자: {}".format(get_prize[0]))
print("커피 당첨자: {}, {}, {}".format(get_prize[1], get_prize[2], get_prize[3]))
print(" -- 축하합니다 -- ")