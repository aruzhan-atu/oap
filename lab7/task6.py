def list_average(values):
    if not values:
        return None
    total = 0
    for value in values:
         total += value
    return total / len(values)

print(list_average([4, 7, 10]))  # 7.0 