def my_rev():
    reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
    i=1
    b=[]
    while i<len(reverse_list)+1:
        b.append(reverse_list[-i])
        i+=1
    print(b)
my_rev()