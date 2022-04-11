# Make a function given a list [‘a’, 1, ‘2’, 5, ‘b’, ‘q’]. Print the last ‘N’ elements of the given list. ‘N’ is accepted from the user.
# Sample Input:
# 1
# Sample Output:
# q 
# Sample Input:
# 3
# Sample Output:
# 5
# b 
# q
def index():
    list1=['a',1,'2',5,"b","q"]
    # print(len(list1))
    index=int(input("Enter the number :"))
    print(list1[index])
index()


# def backindex():
#     list1=['a',1,'2',5,"b","q"]
# # print(len(list1))
#     index=int(input("Enter the number :"))
#     a=(-index)
#     print(list1[-index])
# backindex()
