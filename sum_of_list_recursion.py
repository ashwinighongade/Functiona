def sum_list(lis):
    if len(lis)==1:
        a= lis[0]
        print(a)
        return a
    else:
        a=lis[0] + sum_list(lis[1:])
        print(a)
        return a
sum_list([1, 4, 7, 10])