money = float(input('Введите сумму вклада?'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit1 = float(money*per_cent['ТКБ']/100)
deposit2 = float(money*per_cent['СКБ']/100)
deposit3 = float(money*per_cent['ВТБ']/100)
deposit4 = float(money*per_cent['СБЕР']/100)

deposit = [deposit1, deposit2, deposit3, deposit4]

print('ТКБ -', deposit1)
print('СКБ -', deposit2)
print('ВТБ -', deposit3)
print('СБЕР-', deposit4)
deposit_max = (max(deposit))
print('Максимальная сумма, которую вы можете заработать -', deposit_max)