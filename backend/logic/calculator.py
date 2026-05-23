def calculate_trade(value_a, value_b):
    if value_a > value_b:
        return "WIN"
    elif value_a < value_b:
        return "LOSS"
    return "FAIR"