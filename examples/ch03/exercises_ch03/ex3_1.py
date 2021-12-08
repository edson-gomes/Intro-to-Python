# (Validating user input) Modify the script of Fig. 3.3 to validate its inputs. For any input, if the value entered is other than 1 or 2, keep looping until the user enters a correct value. Use one counter to keep track of the passes, then calculate the number of failures after all the user's inputs have been received.

passes = 0
failures = 0
grades_entered = 0

while grades_entered < 10:
    result = int(input('Enter result (1=pass, 2=fail): '))

    if result == 1:
        passes = passes + 1
        grades_entered += 1
    elif result == 2:
        failures = failures + 1
        grades_entered += 1
    else:
        print('You entered an invalid option. Please, try again.')

print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')
