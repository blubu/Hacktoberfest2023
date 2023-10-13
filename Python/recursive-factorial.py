# recursive function
def fact(n):
    
    # base condition
    if n <= 1:
        return 1
    
    # recursive function
    else:
        return n * fact(n-1)


# user input
num = int(input('Enter number: '))

# printing result
print(f'Factorial of {num} is {fact(num)}')
