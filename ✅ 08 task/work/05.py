res = set()
for a1 in 'БИТКОИН':
  for a2 in 'БИТКОИН':
    for a3 in 'БИТКОИН':
      for a4 in 'БИТКОИН':
        for a5 in 'БИТКОИН':
          for a6 in 'БИТКОИН':
            for a7 in 'БИТКОИН':
              s = a1+a2+a3+a4+a5+a6+a7
              if sorted(s) == sorted('БИТКОИН'):
                res.add(s)
print(len(res))


from itertools import *

k = 0
for x in set(permutations('БИТКОИН', r=7)):
  k += 1
print(k)

print(len(set(permutations('БИТКОИН')))) 