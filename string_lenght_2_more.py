# Write a Python program to count the number of strings where the string length is 2     or more and the first and last characters are the same from a given list of strings.
#  ist=['abc', 'xyz', 'aba', '1221']
# result= 2.
def match_word(list):
    # list=['abc', 'xyz', 'aba', '1221']
    count=0
    i=0
    while i<len(list):
        if len(list[i])>1 and list[i][0]==list[i][-1]:
            count+=1
        i+=1
    print(count)
match_word(['abc', 'xyz', 'aba', '1221'])
     
