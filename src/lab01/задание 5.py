
fio = input('ФИО:').split()
print(f'Инициалы: {fio[0][0]+fio[1][0]+fio[2][0]}.')
sum = 0
for i in fio:
      sum = sum + len(i)
print(f'Длина (символов): {sum + 2}')

 
