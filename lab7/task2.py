total = 0 
for value in numbers:     
    total += value  
if numbers:     
    average = total / len(numbers)     
    print("Қосынды:", total)     
    print(f"Орташа мән: {average:.2f}") 
else:     
    print("Тізім бос") 