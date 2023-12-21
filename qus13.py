# 4. Given a dictionary that maps from letters to frequencies write a python code to create a dictionary that maps from frequencies to letters.
# Sample Input:
# {'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
# Sample Output
# {1: ['a', 'p', 't', 'o'], 2: ['r']}

ab = {'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
c = {}
d = []
for a , b in ab.items():
    d.append(a)
    c[b] = d

print(c)