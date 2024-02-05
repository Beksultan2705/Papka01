myfamily = ('mother','father','sister','brother')
print(myfamily)

print('type of myfamily: ', type(myfamily))
print(myfamily[2])


myfamily_list = list(myfamily)
myfamily_list.append("me")
myfamily = tuple(myfamily_list)
print('Family with me:', myfamily)

myfamily_list = list(myfamily)
myfamily_list.remove('brother')
myfamily = tuple(myfamily_list)
print('Family without brother:', myfamily)
