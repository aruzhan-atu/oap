while True:
    n = int(input("Жиым элементтерінің санын енгізіңіз n (n > 0): "))
    if n > 0:
        break
    print("Қате! Элементтер саны 0-ден үлкен болуы тиіс.")

array = []


print(f"{n} бүтін санды енгізіңіз:")
for i in range(n):
    element = int(input(f"{i}-ші индекс элементі: "))
    array.append(element)


print("Алынған жиым:", array)