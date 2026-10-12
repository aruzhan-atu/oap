array = [5, -3, 8, 2, -1] 

total_sum = 0
for x in array:
    total_sum += x  


arr_max = array[0]
arr_min = array[0]

for x in array:
    if x > arr_max:
        arr_max = x
    if x < arr_min:
        arr_min = x


average = total_sum / len(array)

print("--- 2-тапсырма нәтижесі ---")
print(f"Элементтердің қосындысы: {total_sum}")
print(f"Ең үлкен (максимум) элемент: {arr_max}")
print(f"Ең кіші (минимум) элемент: {arr_min}")
print(f"Орташа арифметикалық мән: {average:.2f}")