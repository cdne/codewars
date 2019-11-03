'''
https://www.codewars.com/kata/5168bb5dfe9a00b126000018

Complete the solution so that it reverses the string value passed into it.

solution('world') # returns 'dlrow'
'''

my_string = 'world'

def solution1(string):
    return string[::-1]

def solution2(string):
    return ''.join([x for x in reversed(string)])

def solution3(string):
    make_list = list(string)
    make_list.reverse()
    return ''.join(make_list)

solution4 = lambda string: string[::-1]
solution5 = lambda string: ''.join([string for string in reversed(string)])

print('Solution1 =', solution1(my_string))
print('Solution2 =', solution2(my_string))
print('Solution3 =', solution3(my_string))
print('Solution4 =', solution4(my_string))
print('Solution5 =', solution5(my_string))