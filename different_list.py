
def my_fun():
    list=[6,7,9,3,1,4]
    list.sort()
    print(list)
    count=0
    i=0
    while i<len(list)-1:
        diff=list[i+1]-list[i]
        if diff>1:
            count+=diff-1
        i+=1
    print(count)
my_fun()

        
        
# max=0
# min=num[0]
# i=0
# while i<len(num):
#     if num[i]>max:
#         max=num[i]
#     if min>num[i]:
#         min=num[i]
#     i+=1
# print(max)
# print(min)
# b=[]
# for j in range(min,max+1):
#     b.append(j)
# print(b)
# c=[]
# count=0
# for j in b:
#     if j not in num:
#         count+=1
#         c.append(j)
# print(c)
# print(count)
# [5,7,9,8,6,4,3,1]
# i=0
# while i<len(list):
#     j=0
#     while j<i:
#         if list[i]<list[j]:
#             print("True")
#         j+=1
#         a=i
#         while a<len(list):
#             if list[i]>list[a]:
                    
