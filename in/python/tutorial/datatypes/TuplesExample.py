"""
A tuple is another sequence data type that is similar to the list.
A tuple consists of a number of values separated by commas. Unlike lists, however,
tuples are enclosed within parentheses.

The main differences between lists and tuples are: Lists are enclosed in brackets
( [ ] ) and their elements and size can be changed, while tuples are enclosed in
parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists

All the methods in the tuple are similar to the methods of list.
"""

string_var = 'string-1'
integer_var = 10
float_var = 10.10
tuple_var = (string_var, integer_var, float_var)
print(tuple_var)
"""
You can not modify tuple. Below line will give an error.
"""
tuple_var[0] = 'another-string'
print(tuple_var)
