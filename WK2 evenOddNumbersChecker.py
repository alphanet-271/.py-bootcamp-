#this program check for odd or even number

def evenOddChecker(number):
    if number % 2 == 0:
        return f'{number} is even'
    else:
        return f'{number} is old'
    
number = int(input("Enter a number: "))
print(evenOddChecker(number))