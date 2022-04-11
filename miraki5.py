# check_numbers naam ka ek function likhiye jo do numbers le aur fir print kare "Dono even hain" agar dono numbers even (2 se divide hote hain) nahi toh print kare "Dono numbers even nahi hai"
# def check():
#     a= int(input("Enter the Number :"))
#     b=int(input("Enter the Number :"))
#     if a%2==0 and b%2==0:
#         print("dono 2 se divisiable hai")
#     else:
#         print("dono 2 se divisiable nahi hai")
        
# check()

def check_number():
    list=[2, 6, 18, 10, 3, 75] 
    list1=[6, 19, 24, 12, 3, 87]
    i=0
    while i<len(list):
        if list[i]%2==0 and list1[i]%2==0:
            print("dono even number hai")
        else:
            print("dono even number nahi hai")
        i+=1
check_number()  