def divs(x):
  # перебор ВСЕХ делителей
  # ds = {1, x}
  # Нетривиальные делители
  ds = set()
  # перебираем все потенциальные делители парами (d, x//d) для случаев, когда x = d *(x//d)
  for d in range(2, int(x**0.5)+1):
    # если х кратно d
    if x % d == 0:
      # добавляем сам делитель (<=кв.корня)
      ds.add(d)
      # добавляем его сомножитель (>кв.корня)
      ds.add(x // d)
      # ds |= {d, x // d}
  # возвращаем сортированный список делителей
  return sorted(ds)

def is_prime(x):
  return x > 1 and all(x % d != 0 for d in range(2, int(x**.5)+1))

# if divs(x) == 2: для всех делителей
# if divs(x) == 0: для нетривиальных делителей



for x in range(326496, 649632+1):
  ds = divs(x)
  nch = [d for d in ds if d % 2 == 1]
  ch = [d for d in ds if d % 2 == 0]
  if len(nch) == len(ch) and len(ch) >= 70:
    print(x, min(d for d in ds if d > 1000))
