"""CHECK IF GIVEN NUMBER IS PALINDROME"""
x=int(input("enter the number"))
x_str=str(x)
if x_str==x_str[::-1]:
    print("true")
else:
    print("false")