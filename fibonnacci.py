def getFibNumber(number):
    if number == 1:
        a=0
        print(a)
        return a
    elif number == 2:
        a=1
        print(a)
        return a
    else:
        a= getFibNumber(number-1) + getFibNumber(number-2)
        print(a)
        return a
number=int(input("Enter the Number :"))
getFibNumber(number)