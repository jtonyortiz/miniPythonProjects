#
#File: collatzSequenceProject.py
#Description: Mini-project that uses and calls the 
#collatz sequence to 'dissolve' a number until
#it outputs a 1.
#Compile: python3 collatzSecuenceProject.py
#

def collatz(num):
    """
    function collatz()
    Description:

    Args:
        num (int): Number to dissolve useing the collatz sequence
    """
    
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1


def collatzProgram(valueInput):
    """
        Function collatzProgram() 
        Calls collats()
        Args:
             valueInput: Integer 
    """    
    
    if valueInput == 1:
        return valueInput
        
    while valueInput != 1:
        valueInput = collatz(valueInput)
        print(valueInput)
        


        
        
print('Enter a number:')
try:
    valueInput = int(input())
except ValueError:
    print('Wrong input: user must enter an integer.')
collatzProgram(valueInput)


