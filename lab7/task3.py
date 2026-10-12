if numbers:     
    minimum = numbers[0]     
    maximum = numbers[0]     
    for value in numbers[1:]:         
        if value < minimum:             
            minimum = value         
            if value > maximum:             
                maximum = value    
    print("Минимум:", minimum)     
    print("Максимум:", maximum) 