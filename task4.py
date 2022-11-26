# Требуется посчитать сумму чётных чисел, 
# расположенных между числами 1 и N включительно.

n = int(input('enter the n:  '))
array = list(range(1,n + 1))
print(f'list of numbers- {array}')
sum = 0
i = 1
for i in array:
    
    if i % 2 == 0:
    
        sum += i
    else:
        i += 1
print(f'sum of even numbers  = {sum}')
  
        



