# bonuses = [100, 200, 300]
# iterator = map(lambda bonus: bonus*2, bonuses)
# print(list(iterator))

list1 = [None, None, 3, 5, None]
print(list1)
new_list = map(lambda listitem: 'X' if listitem is None else listitem, list1)
print(new_list)
