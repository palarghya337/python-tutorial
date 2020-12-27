"""
Identity operators are used to compare the objects, not if they are equal,
but if they are actually the same object, with the same memory location
"""
list1 = ['data1', 'data2']
list2 = ['data1', 'data2']
list3 = list1
print('We have 3 variable as follows,',
      "list1 = ['data1', 'data2']",
      "list2 = ['data1', 'data2']",
      "list3 = list1", sep='\n')
print('-' * 20)
print('list1 is list2:', list1 is list2)
print('list1 is list3:', list1 is list3)
print('list1 is not list2:', list1 is not list2)
