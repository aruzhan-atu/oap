array = [5, -3, 8, 2, -1]

search_value = int(input("Іздеуге арналған санды енгізіңіз: "))
found_index = -1


for i in range(len(array)):
    if array[i] == search_value:
        found_index = i
        break  

print("--- 4-тапсырма нәтижесі ---")
if found_index != -1:
    print(f"Сан табылды! Оның жиымдағы алғашқы индексі: {found_index}")
else:
    print("Сан жиымда жоқ (табылмады).")