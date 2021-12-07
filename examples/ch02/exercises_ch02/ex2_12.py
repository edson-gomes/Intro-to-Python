# (7% Investment Return) Some investment advisors say that it's reasonable to expect a 7% return over the long term in the stock market. Assuming that you begin with $1000 and leav your money invested, calculate and disply how much money you'll have after 10, 20 and 30 years. Use the following formula to determine these amounts:
#
# a = p * (1 + r) ^ n
# where
#   p is the original amount invested
#   r is the rate of return
#   n is the number of years
#   a is the amount on deposit at the end of the n-th year

p = 1000
r = 7 / 100
n = 10      # the value of n will be changed to 20 and 30 later

a = p * (1 + r) ** n
print('After', n, 'years, you will have $', a)

n = 20
a = p * (1 + r) ** n
print('After', n, 'years, you will have $', a)

n = 30
a = p * (1 + r) ** n
print('After', n, 'years, you will have $', a)
