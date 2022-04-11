def my_fun(sum):
    number = [1, 2, 3, 4, 5]
    i=0
    while i<len(number):
        sum=sum+number[i]
        i+=1
    print(sum)
my_fun(0)