# Draw a flowchart to Take 10 numbers as input and create a list of the numbers from the user and update each element of the list according to below rule
# If it is even, then multiply it by 100
# If it is odd, then multiply it by -1 
# Sample Input:
#     23
#     42 
#     41 
#     1
# Sample Output:
#     -23 
#     4200 
#     -41 
#     -1
def even():
    i=0
    b=[]
    while i<10:
        num=int(input("Enter the number :"))
        b.append(num)
        i+=1
    # print(b)
    j=0
    while j<len(b):
        if b[j]%2==0:
            print(b[j]*100)
        else:
            print(-b[j])
        j+=1
even()
        
    
