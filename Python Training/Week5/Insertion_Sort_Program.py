# Get number of elements
n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    element = input(f"Enter string {i+1}: ")
    arr.append(element)

# Insertion Sort
for i in range(1, n):
    key = arr[i]
    j = i - 1

    # Compare strings and sort
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

# Display sorted list
print("Sorted strings in ascending order:")
for item in arr:
    print(item)
