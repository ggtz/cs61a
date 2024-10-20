from doctest import run_docstring_examples
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i<=n:
        if i%3 == 0 and i%5 ==0:
            print('fizzbuzz')
        elif i%3 == 0:
            print('fizz')
        elif i%5 == 0:
            print('buzz')
        else:
            print(i)
        i += 1
    return None


if __name__ == '__main__':
    result = fizzbuzz(16)
    print(result)
    #run_docstring_examples(fizzbuzz, globals(), True)
    # race(5, 7) # After 7 minutes, both have gone 35 steps
    # race(2, 4) # After 10 minutes, both have gone 20 steps