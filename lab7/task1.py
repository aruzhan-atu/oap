text = input("Сандарды бос орынмен енгізіңіз: ") 
numbers = [int(x) for x in text.split()] 
print("Тізім:", numbers)
print("Элементтер саны:", len(numbers)) 
if numbers:     
    print("Бірінші:", numbers[0])     
    print("Соңғы:", numbers[-1]) 