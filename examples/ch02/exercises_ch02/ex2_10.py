# (Arithmetic, Smallest and Largest) Write a script that inputs three integers from the user. Display the sum, average, product, smallest and largest of the numbers. Note that each of these is a reduction in a functional-style programming.

first_integer = int(input('Enter the first integer: '))
second_integer = int(input('Enter the second integer: '))
third_integer = int(input('Enter the third integer: '))

print('\nFirst integer:', first_integer)
print('Second integer:', second_integer)
print('Third integer:', third_integer)


print('\nThe sum of these integers is',
      (first_integer + second_integer + third_integer))
print('The average of these integers is',
      (first_integer + second_integer + third_integer) / 3)
print('The product of these integers is',
      (first_integer * second_integer * third_integer))
print('The smallest of these integers is',
      min(first_integer, second_integer, third_integer))
print('The largest of these integers is',
      max(first_integer, second_integer, third_integer))