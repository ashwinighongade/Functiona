# Write a function to check if a number is even or not.
# def even():
#     num=int(input("Enter the Number :"))
#     if num%2==0:
#         print(num,"is even number")
#     else:
#         print(num,"is not even number")
# even()
'''Q10.Create a function that takes 2 positive integers in form of a string as an input, and outputs the sum (also as a string):

"4",  "5" --> "9"
"34", "5" --> "39"
Notes:

If either input is an empty string, consider it as zero.'''
def sum(num,num1):
    if num != '' and num1 != '':
        print(str(int(num)+int(num1)))
    elif num != '' and num1 == '':
        print(str(int(num)+0))
    elif num1 != '' and num == '':
        print(str(int(num1)+0))
    else:
        print(str(0+0))
sum(input("enter a number:") , input("enter a number :"))
