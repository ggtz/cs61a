def has_digit(n, k):
    while n > 0 :
        t = n % 10
        if(t == k):
            return True
        n = n // 10 
    return False
def unique_digits(n):
    """Return the number of unique digits in positive integer n.
    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    i = n
    count = 0
    while i > 0:
        k = i % 10
        i = i // 10
        if( not has_digit(i,k)):
            count += 1
    return count

if __name__ == '__main__':
    print(unique_digits(8675309))
    print(unique_digits(13173131))
    print(unique_digits(101))



def compose1(f, g):
	return lambda x: f(g(x))
	
f = compose1(lambda x: x * x,
	             lambda y: y + 1)
result = f(12)


