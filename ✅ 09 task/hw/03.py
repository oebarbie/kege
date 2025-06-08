k = 0
for s in open('03.txt'):
    a = [int(x) for x in s.split()]
    a3 = [x for x in a if a.count(x)==3]
    a1 = [x for x in a if a.count(x)==1]
    if len(a3)==3 and len(a1)==3 and sum(a1)/len(a1)<=sum(a3):
        k += 1
print(k)
