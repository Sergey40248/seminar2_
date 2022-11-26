# Требуется найти наименьший натуральный делитель 
# целого числа N, отличный от 1.
#Пример:
#Для n = 15: Ответ: 3
#Для n = 35: Ответ: 5




devident = int(input('enter the devident:  '))

if devident == 1:
    print('invalid input')
        
i = 2
while devident % i != 0:
    i+=1

print(f'smallest natural divisor = {i}')    
        

    


    
        

        

    