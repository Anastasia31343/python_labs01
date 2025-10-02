price = int(input())
discount = int(input())
vat = int(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print('База после скидки',str(base)+'0 ₽')
print('НДС',str(vat_amount)+'0 ₽')
print('Итого к оплате',str(total)+'0 ₽')
