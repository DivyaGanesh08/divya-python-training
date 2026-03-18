n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(input(f"Enter string {i+1}: "))
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("\nSorted array:")
for item in arr:
    print(item)
unique = []
duplicates = []

for i in range(n):
    count = 0
    for j in range(n):
        if arr[i] == arr[j]:
            count += 1
    
    if count == 1:
        unique.append(arr[i])
    else:
        duplicates.append(arr[i])  
print("\nUnique elements:")
for u in unique:
    print(u)
print("\nDuplicate elements (including repeats):")
for d in duplicates:
    print(d)
