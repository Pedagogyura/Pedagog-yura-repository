from pywebio.input import input
from pywebio.output import put_text


def calculate_ticket_price():
    age = input("Введіть ваш вік:", type="number")
    if age < 6:
        price = "безкоштовно"
    elif 6 <= age <= 12:
        price = "50 грн (знижка 50%)"
    elif 13 <= age <= 17:
        price = "75 грн (знижка 25%)"
    elif 18 <= age < 60:
        price = "100 грн (повна ціна)"
    else:
        price = "70 грн (знижка 30%)"

    put_text(f"Вартість квитка: {price}")


if __name__ == "__main__":
    calculate_ticket_price()
