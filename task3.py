#  Задайте список из (2*N+1) элементов, 
# заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. 
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]


n = int(input('enter n:  '))
array = list(range(-n, n + 1))

lengs =int(input('enter length index:  '))
indices = []
for i in range(1,lengs + 1):
    indices.append(int(input('enter the number:  ')))
#print(indices) 
#a = (2, 2, 3, 1, 8)
if len(array) > len(indices):
    result = 1
    for j in indices:
        
        for index in range(len(array)):
            if index == j:
                result *= array[index]

                #print(array[index])
            
    print(result)
    #print(array)

else:
    print('increase(+) n or reduce index(-) ')