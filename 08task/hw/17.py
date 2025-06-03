# from itertools import *

# cnt = 0
# for x in product('ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБА', repeat=11):
#     s = ''.join(x)
#     cnt += 1
#     if s == 'ИНФОРМАТИКА':
#         print(cnt)
#         break

a = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'[::-1]
num = [a.index(x) for x in 'ИНФОРМАТИКА']

def f(x):
  s = 0
  i = len(x) - 1
  for d in x:
    s += d * 33**i
    i -= 1
  return s

print(f(num) + 1)