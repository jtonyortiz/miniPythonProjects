
#
#File: zeroDivide.py
#Description: This program shows division by zero
#Compile: python3 zeroDivide.py

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error Invalid argument.')



print(2)
print(12)
print(0)
print(1)

