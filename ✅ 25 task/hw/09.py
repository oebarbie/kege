def divs(x):
  ds = set()
  for d in range(2, int(x**0.5)+1):
    if x % d == 0:
      ds |= {d, x // d}
  return sorted(ds)

for x in range(112_500_000, 112_550_001):
  ds = divs(x)
  if len(ds) >= 2:
    m = ds[-1] + ds[-2]
    if m%10000 == 1214:
      print(x)
  
  