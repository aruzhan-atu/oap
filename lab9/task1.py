def selection_sort(arr):
    a = arr.copy()
    comps = 0
    swaps = 0
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comps += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return a, comps, swaps, 0

def insertion_sort(arr):
    a = arr.copy()
    comps = 0
    shifts = 0
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            comps += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break
        a[j + 1] = key
    return a, comps, 0, shifts

def bubble_sort(arr):
    a = arr.copy()
    comps = 0
    swaps = 0
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            comps += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    return a, comps, swaps, 0

# Бастапқы мәліметтер (3-нұсқа)
main_list = [9, 9, 3, 12, 3, 1]
edge_tests = [[], [7], [1, 2, 3], [3, 2, 1], [2, 1, 2, 1]]

print("--- Негізгі тізімді сұрыптау нәтижесі ---")
print(f"Бастапқы тізім: {main_list}\n")

# Алгоритмдерді орындау
sel_res, sel_c, sel_sw, sel_sh = selection_sort(main_list)
ins_res, ins_c, ins_sw, ins_sh = insertion_sort(main_list)
bub_res, bub_c, bub_sw, bub_sh = bubble_sort(main_list)
py_sorted = sorted(main_list)

print(f"Selection Sort: {sel_res} | Салыстыру: {sel_c}, Орын алмастыру (Swap): {sel_sw}")
print(f"Insertion Sort: {ins_res} | Салыстыру: {ins_c}, Жылжыту (Shift): {ins_sh}")
print(f"Bubble Sort:    {bub_res} | Салыстыру: {bub_c}, Орын алмастыру (Swap): {bub_sw}")
print(f"Python sorted(): {py_sorted}")
print(f"Тексеру (Барлығы тең бе?): {sel_res == ins_res == bub_res == py_sorted}\n")

print("--- Шекаралық тесттердің нәтижелері ---")
for t in edge_tests:
    print(f"Тест тізім: {t} -> Сұрыпталған: {selection_sort(t)[0]} (Python-мен сәйкес: {selection_sort(t)[0] == sorted(t)})")

