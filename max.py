# [3, 5, 7, 34, 2, 89, 2, 5]
# def max(numbers):
#     i=0
#     max1=0
#     while i<len(numbers):
#         if numbers[i]>max1:
#             max1=numbers[i]
#         i+=1
#     print(max1,"is a max numbers")
# max([3, 5, 7, 34, 2, 89, 2, 5])

def my_fun(max):
    num=[3, 5, 7, 34, 2, 89, 2, 5]
    i=0
    while i<len(num):
        if num[i]>max:
            max=num[i]
        i+=1
    print(max)
my_fun(0)
