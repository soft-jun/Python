from ast import Num
title=""

def gugudan1():
    for i in range(2,10):
        if  i % 2 != 0:
            print("\n%d단" %i)
            for j in range(1, 10):
                    print("%d * %d =  %d" %(i,j,i*j))

def gugudan2():
    for i in range(2,10):
        if i % 2 == 0:
            print("\n%d단" %i)
            for j in range(1, 10):
                    print("%d * %d = %d" %(i,j,i*j))

while True:
    print(title)
    
    Num = int(input("숫자를 입력하세요: "))
    if Num == 1:
        gugudan1()
    elif Num == 2:
        gugudan2()
    elif Num == 3:
        print("프로그램을 종료 합니다.")
        break
    else:
        print("잘못 입력 하셨습니다. 1 ~ 3번 숫자를 입력하세요.")
        continue



        