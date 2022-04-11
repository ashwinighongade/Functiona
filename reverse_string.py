# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Output : "dcba4321".
def reverse(str1):
    str=" "
    i=1
    while i<len(str1)+1:
        str=str+str1[-i]
        i+=1
    print(str)
reverse("1234abcd")
        
        
    
