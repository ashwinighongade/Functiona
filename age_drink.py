# Kids drink toddy.
#     Teens drink coke.
#     Young adults drink beer.
#     Adults drink whisky.
#     Make a function that receive age, and return what they drink

def drink():
    age=int(input("Enter the Age :"))
    if age<14:
        print("drink toddy")
    elif age>14 and age<18:
        print("drink coke")
    elif age>18 and age<21:
        print("drink beer")
    else:
        print("drink whisky")
drink()