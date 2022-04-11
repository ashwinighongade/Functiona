def my_fun(min):
    num=[8, 6, 4, 8, 4, 50, 2, 7]
    i=0
    while i<len(num):
        if num[i]<min:
            min=num[i]
        i+=1
    print(min)
my_fun(8)