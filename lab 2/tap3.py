total_seconds = 3672
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"Нәтиже: {hours} сағат {minutes} минут {seconds} секунд")