def divs(x):
  ds = set()
  for d in range(2, int(x**0.5)+1):
    if x % d == 0:
      ds |= {d, x // d}
  return sorted(ds)

cnt = 0
for x in range(32_500_001, 72_000_000):
  s = [d for d in divs(x) if len(divs(d)) == 0]
  if len(s) != 0 and sum(s) % 145 == 0:
    print(x, sum(s))
    cnt += 1
    if cnt == 7:
      break