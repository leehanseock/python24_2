# num = [0,1,2,3]
# english = ['zero', 'one', 'two']
# sdict = {n:e for n, e in zip(num, english)}
# print(sdict)

#s = 'oh my god!'
# q = list(s)
# print(q)

# matrix = [[3,4,5], [1,2,8], [9,7,6]]
# print(matrix[0])

# new_set = {e**2 for e in range(5,10)}
# print(new_set)

# new_set = {e for e in 'mississippi'}
# print(new_set)
#
# new_set2 = set('mississipii')
# print(new_set2)

vowels = ['a', 'i', 'e', 'o','u']
sentence = '''We don't meet people by accident.
They're meant to cross out path for a reason.'''
words = sentence.lower().replace('\'','').replace('.','').split()
consonats = set(words)
characters = {c for word in words for c in word if c not in vowels}
print(characters)