def divs(x):
    ds = set()
    for d in range(2, int(x**0.5)+1):
        if x % d == 0:
            ds.add(d)
            ds.add(x//d)
    return ds

cnt = 0
for x in range(55_000_000, 60_000_000):
  ds = divs(x)
  if len(ds) > 0:
    # запоминаем наибольший делитель меньше квадратного корня
    pr777 = [d for d in ds
             if len(divs(d)) == 0 and d % 1000 == 777]
    if len(pr777) > 0:
      mn = min(pr777)  
      print(x, mn)
      cnt += 1
      if cnt == 4:
        break