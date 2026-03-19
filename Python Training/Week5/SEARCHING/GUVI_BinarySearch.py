def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1
            
    return -1

try:
    N = int(input("Enter size of array: "))
    
    sorted_arr = list(map(int, input(f"Enter {N} sorted integers: ").split()))
    X = int(input("Enter target value: "))

    result = binary_search(sorted_arr, X)

    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("-1")
except ValueError:
    print("Please enter valid integers.")