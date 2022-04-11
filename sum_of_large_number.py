
# Write a function which converts the input string to uppercase.
# For example:-
# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
# Input sequence contains minimum two elements and every element is an integer.
def add():
    number=[10, 14, 2, 23, 19]
    max=0
    max1=0
    
    i=0
    while i<len(number):
        if number[i]>max:
            max=number[i]
        if number[i]>max1:
            if number[i]!=max:
                max1=number[i]
        i+=1
    a=max+max1
    print("first maximum number",max)
    print("second maximum number",max1)
    print(a)
add()

    
    