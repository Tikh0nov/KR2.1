def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

# Пример использования
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
result = binary_search(sorted_array, target)
if result != -1:
    print(f"Элемент найден на позиции: {result}")
else:
    print("Элемент не найден")
