# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12
def fun():
    str='The quick Brow Fox'
    lower=0
    upper=0
    for i in range(len(str)):
        if(str[i]>="A" and str[i]<="Z"):
            upper+=1
        elif (str[i]>="a" and str[i]<="z"):
            lower+=1
    print("No. of Uppercase characters",upper)
    print("No. of Lowercase characters",lower)
fun()