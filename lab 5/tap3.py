array = [5, -3, 8, 2, -1]

pos_count = 0   
neg_count = 0  
even_count = 0 

for x in array:
    if x > 0:
        pos_count += 1
    elif x < 0:
        neg_count += 1
        
    if x % 2 == 0:
        even_count += 1

print("--- 3-тапсырма нәтижесі ---")
print(f"Оң сандар саны: {pos_count}")
print(f"Теріс сандар саны: {neg_count}")
print(f"Жұп элементтер саны: {even_count}")