# Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
# Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7
# The original list is : [15, 81, 11, 234]
# def sum():
#     list=[12, 67, 98, 34]
#     # sum=0
#     list1=[]
#     i=0
#     while i<len(list):
#         a=str(list[i])
#         sum=0
#         j=0
#         while j<len(a):
#             sum=sum+int(a[j])
#             j+=1
#         list1.append(sum)
#         i+=1
#     print(list1)
# sum()
        
def sum_digit(number):
    sum=0
    rem=0
    while number!=0:
        rem=number%10
        sum+=rem
        number=number//10
    print(sum)
sum_digit(123)
