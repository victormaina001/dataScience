list1=['a','b','c']
list2=[1,2,3]
print([pair for pair in zip(list1,list2)])


#You can also “unzip” a list using a strange trick:
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
