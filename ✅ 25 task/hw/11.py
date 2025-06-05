def divs(x):
    res = set()
    for d in range(2, int(x*0.5)+1):
        if x%d == 0:
            res |= {d, x // d}
    return sorted(res)

cnt = 0
for x in range(39345679, -1, -1):
  if x % 2 == 0 and x % 3 == 0 and x % 5 == 0 and x % 7 == 0:
    ds = divs(x)
    if 76 <= len(ds) <= 88:
      print(x, len(ds))
      cnt += 1
      if cnt == 10:
        break