# Your task is to create function is Divided By (or is_divide_by) to check if an integer number is divisible by each out of two arguments.
# A few cases:
# (-12, 2, -6)  ->  true
# (-12, 2, -5)  ->  false
# (45, 1, 6)    ->  false
# (45, 5, 15)   ->  true
# (4, 1, 4)     ->  true
# (15, -5, 3)   ->  true
def is_divide_by(num,a,b):
    if num%a==0 and num%b==0:
        print("True")
    else:
        print("False")
is_divide_by(-12, 2, -6)