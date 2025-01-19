# #8.1
# a=int(input("Enter a number"))
# b=int(input("Enter a number"))
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print('division by zero not possible')

#8.2
# a1=int(input("Enter the string:"))
# a2=int(input("Enter the string:"))
# try:
#     print(a1+a2)
# except ValueError:
#     print("Invalid input")

#8.3
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
try:
    print(a+b)
except ValueError:
    print("Invalid input")
finally:
    print("The program has ended")
