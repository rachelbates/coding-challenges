"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""

def fit_to_width(string, limit):
    """Print string within a character limit."""
    #insert new_line break where there is a space as close to the limit as possible
    new_line = '\n'
    new_string = ''
    at = limit + 1
    prev_at = 0
    while at < len(string) - 1:
        if string[at] != ' ':
            at -= 1
        else:
            new_string += string[prev_at:at] + new_line
            prev_at = at + 1
            at += limit + 1

    new_string += string[prev_at:]
    
    print(new_string)
            


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')