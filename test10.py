a=int(input("숫자를 입력하세요: "))
b=int(input("숫자를 입력하세요: "))
c=int(input("숫자를 입력하세요: "))

def middle_value(a,b,c):
    if(b>=a and c<=a) or (b<=a and c>=a):
        return a
    elif(a>b and c<b) or (a<b and c>b):
        return b
    else:
        return c
print("중간값: ", middle_value(a,b,c))