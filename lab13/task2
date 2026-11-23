def process_expense(balance, expense):
    try:
        if isinstance(balance, bool) or isinstance(expense, bool):
            raise TypeError("Логикалық мән (bool) енгізуге болмайды.")
        if not isinstance(balance, (int, float)) or not isinstance(expense, (int, float)):
            raise TypeError("Баланс пен шығыс сан болуы керек.")
        if balance < 0 or expense < 0:
            raise ValueError("Сома теріс сан болмауы тиіс.")
        if expense > balance:
            raise ValueError("Шоттағы қаражат жеткіліксіз (артық шығыс).")
            
        new_balance = balance - expense
        return new_balance
    except (ValueError, TypeError) as e:
        return f"Қате: {e}"

if __name__ == "__main__":
    # 1. Қалыпты жағдай
    print("Тест 1 (Қалыпты):", process_expense(10000, 2500))
    # 2. Шекаралық жағдай (қосымша тест: барлық қаражатты шешу)
    print("Тест 2 (Шекаралық):", process_expense(1000, 1000))
    # 3. Қате жағдай (артық шығыс)
    print("Тест 3 (Артық шығыс):", process_expense(1000, 1500))
    # 4. Ерекше/қате жағдай (теріс сома)
    print("Тест 4 (Теріс сома):", process_expense(500, -1))
