# # user definate funcion
# # ● No argrument and return

# from ssl import ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION


# def my_fun():
#     a=int(input("Enter the number :"))
#     b=int(input("Enter the number :"))
#     print(a+b)
# my_fun()

# # ● with argrument and return
# def my_fun(a,b):
#     c=a+b
#     return c
# my_fun(5,3)

# # ● No argrument and with return
# def my_fun():
#     a=int(input("Enter the number :"))
#     b=int(input("Enter the number :"))
#     c=a+b
#     return c
# my_fun()

# # ● with argrument and no return
# def my_fun(a,b):
    
#     print(a+b)
# my_fun(5,8)





# def add(a=5,b=10):
#     c=a+b
#     return c
# print(add(a=34,b=7))
    
# def add(a,b):
#     c=a+b
#     return c
# print(add(34,7))

# def add(a,b):
#     c=a+b
#     return c
# print(add(b=34,a=7))

def add(*b):
    sum=0
    i=0
    while i<len(b):
        sum+=b[i]
        i+=1
    print(sum)
add(1,2,3,4,5)


def my_fun(**b):
    for i in b.items():
        print(i)
my_fun(num=5,colors="blue",fruits="apple")