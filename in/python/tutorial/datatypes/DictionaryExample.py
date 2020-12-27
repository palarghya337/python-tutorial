"""
Python's dictionaries are kind of hash table type. They work like associative arrays
or hashes found in Perl and consist of key-value pairs. A dictionary key can be almost
any Python type, but are usually numbers or strings. Values, on the other hand, can be
any arbitrary Python object.

Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([])
"""
dictionary_var = {'key-0': 'value-0', 1: 'value-1'}
"""
The keys() method to display all the available keys inside a dictionary.
"""
print("|Example key(): ", dictionary_var.keys())
"""
The values() method to display all the available values present inside a dictionary.
"""
print('|Example values(): ', dictionary_var.values())
"""
In the dictionary it is possible to not to have any key or value. Below is the example for that.
"""
dictionary_var['key-2'] = None
dictionary_var[None] = 'value-3'
print('|Not having key or value: ', dictionary_var)
"""
The pop method here will take key as a parameter and will remove the key and value from the
dictionary and returns the value associated with that key.
"""
popped_data = dictionary_var.pop(None)
print('|Example pop(): ', dictionary_var, '| popped data: ', popped_data)
"""
The popitem() method remove and return a (key, value) pair as a 2-tuple.
Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.
"""
popped_data = dictionary_var.popitem()
print('|Example popitem(): ', popped_data)
"""
The fromkeys() method creates a new dictionary from the given sequence of elements with a
value provided by the user. This method takes two parameters:

sequence - sequence of elements which is to be used as keys for the new dictionary
value (Optional) - value which is set to each each element of the dictionary
"""
sub_dictionary = dictionary_var.fromkeys(dictionary_var.keys(), 'new-value')
print('|Example fromkeys(): ', sub_dictionary)
"""
We can also create dictionary from any given list of keys, something like this.
"""
key_list = ['a', 'e', 'i', 'o', 'u']
another_dictionary = {key: 'default-value' for key in key_list}
print('|Dictionary from set: ', another_dictionary)
"""
The items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
"""
print('|Example items(): ', dictionary_var.items())
"""
The setdefault() method returns the value of a key (if the key is in dictionary).
If not, it inserts key with a value to the dictionary. If key is present with some value in it and
default value is provided then the default value will be ignored.

This method takes maximum two parameters: 
key - the key to be searched in the dictionary
default_value (optional) - key with a value default_value is inserted to the dictionary if the key is
not in the dictionary.

If not provided, the default_value will be None
"""
default_value = 'default-value'
dictionary_var.setdefault('key-5', default_value)
dictionary_var.setdefault('key-0', default_value)
print('|Example setdefault(): ', dictionary_var)
"""
The update() method updates the dictionary with the elements from the another dictionary object or
from an iterable of key/value pairs. This method adds element(s) to the dictionary if the key is
not in the dictionary. If the key is in the dictionary, it updates the key with the new value.
It doesn't return any value.
"""
another_dictionary = {'key-0': 'updated-value'}
dictionary_var.update(another_dictionary)
print('|Example update(): ', dictionary_var)
