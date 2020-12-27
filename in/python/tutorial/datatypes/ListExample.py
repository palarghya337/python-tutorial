"""
Lists are the most versatile of Python's compound data types. A list contains items
separated by commas and enclosed within square brackets ([]). To some extent, lists
are similar to arrays in C. One difference between them is that all the items
belonging to a list can be of different data type.

The values stored in a list can be accessed using the slice operator ([ ] and [:])
with indexes starting at 0 in the beginning of the list and working their way to
end -1. The plus (+) sign is the list concatenation operator, and the asterisk (*)
is the repetition operator.
"""

string_var = 'string-1'
integer_var = 10
float_var = 10.10
list_var = [string_var, integer_var, float_var]
another_list_var = ['another-data1', 'another-data2']
print('|main-list: ', list_var)
# We can add/append data into a list. Below is the example for that
list_var.append('string-2')
print('|append() example: ', list_var)
# You can also update data inside a list. Below is the example for that.
list_var[0] = 'updated-data'
print('|Updating data: ', list_var)
"""
The index() method of a list is used to find the index of a specific data.
"""
print('|index() example: ', list_var.index(10))
"""
The extend() method of a list is used to modify the existing list with new new data from another list.
"""
list_var.extend(another_list_var)
print("|extend() example:", list_var)
"""
The insert() method takes two parameters:

index - the index where the element needs to be inserted
element - this is the element to be inserted in the list
"""
inserted_data = 'inserted-data'
list_var.insert(2, inserted_data)
print('|insert() example: ', list_var)
"""
The remove() method removes the first matching element (which is passed as an argument) from the list.
"""
list_var.remove(inserted_data)
print('|remove() example: ', list_var)
"""
The pop() method removes the item at the given index from the list and returns the removed item.
"""
popped_data = list_var.pop(0)
print('|pop() example: ', list_var, '| popped data: ', popped_data)
"""
The reverse() method reverses the elements of the list.
"""
list_var.reverse()
print('|reverse() example: ', list_var)
