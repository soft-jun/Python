def find_min_max(A):
    min = A[0]
    max = A[0]
    for i in range(1, len(A)) :
        if max < A[i] : max = A[i]
        if min < A[i] : min = A[i]
    return min, max

    import random
    list = []
    for i in (1,10):
        lists = random.randint(1,101)
        list.append(lists)
    x, y = find_min_max(list)
    print("(min,max) = ", (x,y))