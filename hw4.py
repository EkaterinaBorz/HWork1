#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
#если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input('Введите длину шоколадки в дольках: '))
m = int(input('Введите ширину шоколадки в дольках: '))
k = int(input('Введите количество долек, которе необходимо отломить: '))
if k % m == 0 or k % n == 0 and k < m * n:
    print('Поздравляем! Ваша шоколадка разделена:) ')
else: 
    print('Увы, но так поделить шоколадку не получится:( ')