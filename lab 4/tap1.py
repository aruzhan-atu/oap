arnaiy_san = int(input("Бүтін сан енгізіңіз: "))
san = abs(arnaiy_san)
sum = 0
while san > 0:
    cifr = san % 10      # Соңғы цифрды алу
    sum += cifr      # Қосындыға қосу
    san = san // 10 
print(f"{arnaiy_san} санының цифрларының қосындысы: {sum}")


