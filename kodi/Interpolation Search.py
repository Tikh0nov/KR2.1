def interpolation_search(arr, lo, hi, x):
    if lo <= hi and x >= arr[lo] and x <= arr[hi]:
        pos = lo + (((hi - lo) * (x - arr[lo])) // (arr[hi] - arr[lo]))
        
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            return interpolation_search(arr, pos + 1, hi, x)
        if arr[pos] > x:
            return interpolation_search(arr, lo, pos - 1, x)
    
    return -1

# Пример использования
arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
target = 18
result = interpolation_search(arr, 0, len(arr) - 1, target)
if result != -1:
    print(f"Элемент найден на позиции: {result}")
else:
    print("Элемент не найден")
