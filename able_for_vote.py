# Write a function to tell user if he/she is able to vote or not.( Consider minimum age of voting to be 18. )

def vote():
    age=int(input("Enter the Age :"))
    if age>=18:
        print("He/She is able to Vote")
    else:
        print("He/She is not able to Vote")
        
vote()
        

