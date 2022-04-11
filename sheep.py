# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the 



def sheep():
    list1 = [True,  True,  True,  False,
    True,  True,  True,  True ,
    True,  False, True,  False,
    True,  False, False, True ,
    True,  True,  True,  True ,
    False, False, True, None]
    i = 0
    c = 0
    while i < len(list1):
        if list1[i] == True or list1[i]== None :
            c+=1
        i+=1
    print(c)
sheep()