# Numbers ending with zeros are boring.
# They might be fun in your world, but not here
# Get rid of them. Only the ending ones.

# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
def fun(num):
    if num%10!=0:
        print(num)
    else:
        fun(num=num//10)
fun(int(input("enter a number:")))
