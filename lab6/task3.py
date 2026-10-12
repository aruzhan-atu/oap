def is_passed(score):
    if score < 0 or score > 100:
        return None
    return score >= 50

# Мәндерді тексеру
print(is_passed(49))   # Нәтиже: False
print(is_passed(50))   # Нәтиже: True
print(is_passed(100))  # Нәтиже: True
print(is_passed(120))  # Нәтиже: None (диапазоннан тыс)