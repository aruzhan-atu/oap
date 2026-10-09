array = [5, -3, 8, 2, -1]

print("--- 5-тапсырма нәтижесі ---")
if len(array) < 2:
    print("Жиым ұзындығы 2-ден кем. Екінші үлкен элементті анықтау мүмкін емес.")
else:
    
    first_max = array[0]
    second_max = None
    
    for i in range(1, len(array)):
        x = array[i]
        if x > first_max:
            second_max = first_max
            first_max = x
        elif x < first_max:
            if second_max is None or x > second_max:
                second_max = x
                
    if second_max is None:
        print("Жиымдағы барлық элементтер бірдей, екінші үлкен элемент жоқ.")
    else:
        print(f"Шамасы бойынша екінші элемент (екінші максимум): {second_max}")