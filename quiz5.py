from random import *
customer = 0
for users in range(1,51):
    time = randrange(5, 51)
    if time>=5 and time<=15:
        print(f"[O] {users}번째 손님 (소요시간 : {time}분)")
        customer+=1
    else:
        print(f"[ ] {users}번째 손님 (소요시간 : {time}분)")
print(f"총 탑승 승객 : {customer}분")