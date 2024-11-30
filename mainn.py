import menu
import phrases


client_name = input("Добрий день, раді вас бачити у ресторані *Дача*. Як вас звуть? >> ").strip()
print("Наше меню на сьогодні:")

borsh_quantity = input(f"{phrases.borsh} по ціні {menu.borsh_price}. Скільки порцій бажаєте? >> " ).strip()
borsh_quantity = int(borsh_quantity)
borsh_total_price = borsh_quantity * menu.borsh_price

dumpling_quantity = input(f"{phrases.dumpling} по ціні {menu.dumpling_price}. Скільки порцій бажаєте? >> " ).strip()
dumpling_quantity = int(dumpling_quantity)
dumpling_total_price = dumpling_quantity * menu.dumpling_price

caviar_quantity = input(f"{phrases.caviar} по ціні {menu.caviar_price}. Скільки порцій бажаєте? >> " ).strip()
caviar_quantity = int(caviar_quantity)
caviar_total_price = caviar_quantity * menu.caviar_price

icecream_quantity = input(f"{phrases.icecream} по ціні {menu.icecream_price}. Скільки порцій бажаєте? >> " ).strip()
icecream_quantity = int(icecream_quantity)
icecream_total_price = icecream_quantity * menu.icecream_price

lemonade_quantity = input(f"{phrases.lemonade} по ціні {menu.lemonade_price}. Скільки порцій бажаєте? >> " ).strip()
lemonade_quantity = int(lemonade_quantity)
lemonade_total_price = lemonade_quantity * menu.lemonade_price

print("Також сьогодні в нашому ресторані знижка 15% на всі блюда.")

total_price = (borsh_total_price + dumpling_total_price + caviar_total_price + icecream_total_price + lemonade_total_price)
discount = 0.15
discounted_price = total_price * (1 - discount)

print("\nВаш чек:")
print(f"Клієнт: {client_name} {discounted_price}")










