# Write a Python program to generate and print a list of first and last 5 elements where 
#   the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).
def my_fun():
    b=[]
    
    i=1
    while i<=30:
        b.append(i**2)
        i+=1
    print(b[:5])
    print(b[-5:])
my_fun()
    