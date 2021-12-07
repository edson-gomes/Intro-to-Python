# (Separating Digits in an Integer) Write a script that inputs a five-digit integer from the user. Separate the number into its individual digits. Print them separated by three spaces each. For example, if the user types in the number 42399, the script shoud print
#
# > 4   2   3   3   9
#
# Assume that the user enters the correct number of digits. Use both the floor division and remainder operations to "pick off" each digit.

integer = int(input('Enter a number between 10000 and 99999: '))

print(integer // 10000, end='   ')
integer = integer % 10000
print(integer // 1000, end='   ')
integer = integer % 1000
print(integer // 100, end='   ')
integer = integer % 100
print(integer // 10, end='   ')
integer = integer % 10
print(integer)
