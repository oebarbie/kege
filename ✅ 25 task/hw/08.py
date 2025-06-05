def divs(x):
  ds = set()
  for d in range(2, int(x**0.5)+1):
    if x % d == 0:
      ds |= {d, x // d}
  return sorted(ds)

cnt=0
for x in range(310_001, 410_000):
  ds = [d for d in divs(x) if len(divs(d)) == 0]
  if len(ds) > 0:
    a = sum(ds)//len(ds)
    if a%6 == 0 and a%10 != 4:
      print(x, a)
      cnt += 1
      if cnt == 6:
        break