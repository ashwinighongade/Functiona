# Write a Python function to find the Max of three numbers
def max_num():
    x=int(input("Enter the first Number :"))
    y=int(input("Enter the second Number :"))
    z=int(input("Enter the third Number :"))
    if x>y and x>z:
        print(x,"is max Number")
    elif y>z and y>x:
        print(y,"is max Number")
    elif z>x and z>y:
        print(z,"is max Number")
        
max_num()


        
    