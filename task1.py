# ) Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('enter the number\n'))
count = 0
f = 1
a = []       #чтобы вывод выглядел как в задании 
while count < n:
    count += 1
    f *= count
   
    a.append(f)  #чтобы вывод выглядел как в задании 
print(a)

