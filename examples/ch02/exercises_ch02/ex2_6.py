# (Odd or Even) Use if statements to determine whether an integer is odd or even. [Hint: Use the remainder operator. An even number is a multiple of 2. Any multiple of 2 leaves a remainder of 0 when divided by 2.]

integer = int(input('Enter an integer number: '))

if (integer % 2) == 0:
    print(integer, 'is an even number.')
if (integer % 2) != 0:
    print(integer, 'is an odd number.')
