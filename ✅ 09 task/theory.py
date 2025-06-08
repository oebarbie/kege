# открываем excel таблицу
# копируем данные в блокнот
# сохраняем на рабочий стол
# 

for s in open('09.txt'):
    a = sorted([int(x) for x in s.split()])