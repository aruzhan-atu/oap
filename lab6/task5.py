def subtotal(price, quantity):
    return price * quantity

def discount_amount(amount, rate):
    return amount * rate

def final_price(price, quantity, rate=0):
    amount = subtotal(price, quantity)
    return amount - discount_amount(amount, rate)

# Төрт түрлі тестілік жағдаймен тексеру
print(final_price(2500, 3, 0.10)) # 10% жеңілдік -> 6750.0
print(final_price(1000, 2, 0.00)) # 0% жеңілдік -> 2000.0
print(final_price(5000, 1, 1.00)) # 100% жеңілдік -> 0.0
print(final_price(1500, 1, 0.20)) # 20% жеңілдік -> 1200.0