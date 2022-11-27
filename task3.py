#  Задайте список из (2*N+1) элементов, 
# заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. 
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

n = int(input('enter n:  '))
array = list(range(-n, n + 1))
a = (2, 2, 3, 1, 8)
result = 1
for i in a:
    
    for index in range(len(array)):
        if index == i:
            result *= array[index]

            #print(array[index])
        
print(result)
#print(array)