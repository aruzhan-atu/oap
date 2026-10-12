import math

def eesepte_uzundyq(radius):
    """Шеңбердің ұзындығын (периметрін) есептеу: L = 2 * pi * r"""
    return 2 * math.pi * radius

def eesepte_audan(radius):
    """Шеңбердің ауданын есептеу: S = pi * r^2"""
    return math.pi * (radius ** 2)

def darysterdi_tekseru(radius_str):
    """Кіріс деректерін тексеру және есептеулерді орындау функциясы"""
    try:
        radius = float(radius_str)
        # Радиустың оң болуын тексеру
        if radius <= 0:
            return "Қате: Радиус тек оң сан болуы керек!"
        
        uzundyq = eesepte_uzundyq(radius)
        audan = eesepte_audan(radius)
        
        return f"Радиус: {radius} -> Ұзындығы: {uzundyq:.2f}, Ауданы: {audan:.2f}"
    except ValueError:
        return "Қате: Енгізілген мән сан емес!"

# Бағдарламаны 4 түрлі тестілік жағдаймен тексеру
test_cases = ["5", "12.5", "-3", "0"]

print("--- Бағдарламаны тестілеу нәтижесі ---")
for i, test in enumerate(test_cases, 1):
    print(f"{i}-ші тест (Енгізілген мән: {test}):")
    print(darysterdi_tekseru(test))
    print("-" * 40)
