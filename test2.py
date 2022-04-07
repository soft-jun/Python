import random as rd

num = rd.randomint(1, 50)
print(num)

num = rd.randrange(0,50,2)
print(num)

list = rd.random.sample(range(100,200), 6)
print(list)


num = rd.sample(num,5)
print(num)

min=num[0]

# 3)num이라는 리스트를 선언해서 숫자 10개 넣기
# 2)num리스트에서 숫자 6개 랜덤으로 뽑아서 출력
# 1)출력한 숫자 중 가장 작은수 출력

