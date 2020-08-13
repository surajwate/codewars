""" 
kata  : https://www.codewars.com/kata/525f50e3b73515a6db000b83
Level : 6kyu

Create Phone Number
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

Coder : Suraj (https://github.com/surajwate)
"""


def create_phone_number(nums):
    pn = '('
    for i in range(3):
        pn += str(nums[i])
    pn = pn + ') '
    
    for i in range(3, 6):
        pn += str(nums[i])
    pn = pn + '-'
    
    for i in range(6, 10):
        pn += str(nums[i])

    return(pn)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
