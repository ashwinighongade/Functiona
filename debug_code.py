# def sum():
#  print(12+13)
# sum()


# def welcome():
#     print("Welcome to function")
# welcome()

# def isEven():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number")
        
# isEven()    

# def say_hello_language(name, language):
#     if language == "hindi":
#         print("Namaste ", name)
#         print("Aap kaise ho?")
#     elif language == "punjabi":
#         print("Sat sri akaal ", name)
#         print("Tuhada ki haal hai?")
#     else:
#         print("Hello ", name)
#         print("How are you?")
# say_hello_language("Rishabh", "punjabi")
# say_hello_language("Armaan", "english")
# say_hello_language("Abhishek", "french")
# say_hello_language("Kavay", "hindi")

# def greet(*names):
#     for name in names:
#         print("Welcome"+" ", name)
# greet("Rinki", "Vishal", "Kartik", "Bijender")

# def info(name, age ="15" ):
#     print(name + " is " + age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18")

def studentDetails(name,currentMilestone,mentorName):
    print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)


studentDetails("Nilam","list theory","loop")