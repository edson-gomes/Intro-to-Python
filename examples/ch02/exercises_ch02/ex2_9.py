# (Integer Value of a Character) Here's a peek ahead. In this chapter, you learned about strings. Each of a string's characters has an integer representation. The set of characters a computer uses together with the characters' integer representations is called that computer's character set. You can indicate a character value in a program by enclosing that character in quotes, as in 'A'. To determine a character's integer value, call the built-in function ord(). 
# Display the integer equivalents of B C D b c d 0 1 2 $ * + and the space character.

print('The integer equivalent of B is', ord('B'))
print('The integer equivalent of C is', ord('C'))
print('The integer equivalent of D is', ord('D'))
print('The integer equivalent of b is', ord('b'))
print('The integer equivalent of c is', ord('c'))
print('The integer equivalent of d is', ord('d'))
print('The integer equivalent of 0 is', ord('0'))
print('The integer equivalent of 1 is', ord('1'))
print('The integer equivalent of 2 is', ord('2'))
print('The integer equivalent of $ is', ord('$'))
print('The integer equivalent of * is', ord('*'))
print('The integer equivalent of + is', ord('+'))
print('The integer equivalent of the space character is', ord(' '))