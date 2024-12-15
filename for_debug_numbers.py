from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP


def format_price(price):
    return Decimal(price).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def validate_quantity(quantity):
    if not quantity.isdigit():
        raise ValueError("Кількість повинна бути цілим числом.")
    return int(quantity)


item_1_title = input('Назва 1-го товару: ').strip()
item_1_quantity = validate_quantity(input('Кількість 1-го товару: '))
item_1_price = Decimal(input('Ціна 1-го товару: '))
item_1_total = format_price(item_1_quantity * item_1_price)

item_2_title = input('Назва 2-го товару: ').strip()
item_2_quantity = validate_quantity(input('Кількість 2-го товару: '))
item_2_price = Decimal(input('Ціна 2-го товару: '))
item_2_total = format_price(item_2_quantity * item_2_price)

total_cost = format_price(item_1_total + item_2_total)

print(f'\n\n~~~ ФІСКАЛЬНИЙ ЧЕК ~~~')
print(f'1. {item_1_title}: {item_1_quantity} x {format_price(item_1_price)} = {item_1_total}')
print(f'2. {item_2_title}: {item_2_quantity} x {format_price(item_2_price)} = {item_2_total}')
print(f'ВСЬОГО: {total_cost}')
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
