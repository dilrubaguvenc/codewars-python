# Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised to the number of digits of each numbers, so, for example:

#   3 -->    15  (  3 * 5¹)
#  10 -->   250  ( 10 * 5²)
# 200 --> 25000  (200 * 5³)
#   0 -->     0  (  0 * 5¹)
#  -3 -->   -15  ( -3 * 5¹)


# my solution 

def multiply(n):
    if n == 0:
        return 0
    num_digits = len(str(abs(n)))
    
    result = n * (5 ** num_digits)
    
    return result

def multiply(n):
    return n * 5 ** len(str(abs(n)))