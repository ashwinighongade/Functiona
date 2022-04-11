# I would like to be able to pass an array with two elements to my swapValues function to swap the values. However it appears that the values aren't changing.
def swap(num):
    # num=[1,3,5,6,8,9,7,4,2]
    tem=num[2]
    num[2]=num[5]
    num[5]=tem
    print(num)
swap([1,3,5,6,8,9,7,4,2])