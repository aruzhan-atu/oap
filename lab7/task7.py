# 1-функция: Орташа бағаны және 50-ден төмен бағалар санын есептеу
def analyze_grades(grades):
  if not grades:
    return 0, 0
  avg_grade = sum(grades) / len(grades)
  low_grades_count = sum(1 for g in grades if g < 50)
  return avg_grade, low_grades_count


# 2-функция: Ең жоғары бағаны табу
def get_max_grade(grades):
  if not grades:
    return None
  return max(grades)


# --- 4 тестілік жағдаймен тексеру (Test cases) ---
test_cases = [
    [45, 60, 85, 40, 95],  # 1-тест
    [30, 25, 49],  # 2-тест (барлығы 50-ден төмен)
    [80, 90, 100],  # 3-тест (50-ден төмен жоқ)
    [50, 50, 75],  # 4-тест
]

for i, test in enumerate(test_cases, 1):
  avg, low_count = analyze_grades(test)
  max_g = get_max_grade(test)
  print(f'Тест {i}: {test}')
  print(f'  - Орташа баға: {avg:.2f}')
  print(f'  - Ең жоғары баға: {max_g}')
  print(f'  - 50-ден төмен бағалар саны: {low_count}\n')
