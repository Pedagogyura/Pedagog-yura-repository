bread = input('Enter quantity of bread loafes >>').strip()
bread_price = 25
bread_quantity = int(bread)
total_bread = bread_quantity * bread_price

butter = input('Enter quantity of butter , g >> ').strip()
butter_price = 320
butter_quantity = float(butter)
total_butter = butter_quantity * butter_price

total = total_bread + total_butter
total = round(total , -1)

print(total)
print('*' * 50)
print('RECEIPT')
print(f'Total of money for your purchase = {total}')
print('=' * 50)
