# Bubble Sort Program

def bubble_sort(arr, order="asc"):
    n = len(arr)
    swap_count = 0
    sorted_arr = arr.copy()

    for i in range(n):
        for j in range(0, n - i - 1):
            
            if order == "asc":
                if sorted_arr[j] > sorted_arr[j + 1]:
                    # Swap
                    sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                    swap_count += 1

            elif order == "desc":
                if sorted_arr[j] < sorted_arr[j + 1]:
                    # Swap
                    sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                    swap_count += 1

    return sorted_arr, swap_count


# Input
n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

# Ascending Order
asc_sorted, asc_swaps = bubble_sort(arr, "asc")
print("Ascending Order:", asc_sorted)
print("Number of swaps (Ascending):", asc_swaps)

# Descending Order
desc_sorted, desc_swaps = bubble_sort(arr, "desc")
print("Descending Order:", desc_sorted)
print("Number of swaps (Descending):", desc_swaps)