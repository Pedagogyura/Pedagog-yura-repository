def calculate_total(prices: list[float]) -> float:
    """
    Calculates the total sum of a list of prices.

    :param prices: List of item prices.
    :return: The total sum of the prices.
    """
    return sum(prices)

def get_unique_items(items: list[str]) -> list[str]:
    """
    Returns a list containing only unique strings from the input list.

    :param items: List of strings with possible duplicates.
    :return: List of unique strings.
    """
    return list(set(items))

def can_afford(budget: float, price: float) -> bool:
    """
    Checks if the budget is sufficient to purchase an item at the given price.

    :param budget: Available budget.
    :param price: Price of the item.
    :return: True if the budget is greater than or equal to the price, otherwise False.
    """
    return budget >= price
