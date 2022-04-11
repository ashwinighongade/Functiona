def factorial(number):
    if number==1:
        a=1
        print(a)
        return a
    else:
        a=(number * factorial(number - 1))
        print(a)
        return a
number=int(input("Enter the number :"))
factorial(number)
