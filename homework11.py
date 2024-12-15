def filter_long_strings(strings):
    result = [s for s in strings if len(s) > 10]
    print("Результат:", result)
    return result


strings_list = ["коротка", "дуже-довга-стрічка", "ще одна", "найдовша-стрічка"]
filter_long_strings(strings_list)
