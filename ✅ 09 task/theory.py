# открываем excel таблицу
# копируем данные в блокнот
# сохраняем на рабочий стол
# 

k = 0

for s in open('09.txt'):
    a = [int(x) for x in s.split()]
    a = sorted(a)
    if (a[-1]*a[0])**2 > 3*a[1]*a[2]*a[3]:
        k += 1
print(k)