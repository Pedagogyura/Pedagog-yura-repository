car_details = {
    "model": "Toyota C-HR Hybrid",
    "price": 1_905_290,
    "engine_volume": 1987,
    "gross_weight": None,
    "max_speed": None,
    "interior_features": [
        "Multifunctional 8\" touchscreen display",
        "Support for Apple CarPlay and Android Auto",
        "Heated steering wheel",
        "Parking assistance system with a rearview camera"
    ],
    "luggage_compartment": {
        "trunk_volume": None,
        "folded_seat_volume": None
    },
    "max_trailer_weight_with_brakes": None
}

car_model = car_details["model"]
car_price = car_details["price"]
first_interior_feature = car_details["interior_features"][0]
folded_seat_volume = car_details["luggage_compartment"]["folded_seat_volume"]

print(f"Модель: {car_model}")
print(f"Ціна: {car_price}")
print(f"Перша опція інтер'єру: {first_interior_feature}")
print(f"Об'єм багажника зі складеними сидіннями: {folded_seat_volume}")
