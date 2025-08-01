import matplotlib.pyplot as plt  


def merge_sort(arr):		
    if len(arr) > 1:        
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]
        
	# Recursively sort both halves
        merge_sort(left_arr)
        merge_sort(right_arr)
	
        l = 0
        r = 0
        i = 0 

	# Merge the sorted halves back into the main array
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] <= right_arr[r]:
                arr[i] = left_arr[l]
                l += 1
            else:
                arr[i] = right_arr[r]
                r += 1
            i += 1

	# Copy any remaining elements from left_arr
        while l < len(left_arr):
            arr[i] = left_arr[l]
            l += 1
            i += 1

	# Copy any remaining elements from reght_arr
        while r < len(right_arr):
            arr[i] = right_arr[r]
            r += 1
            i += 1


arr_test = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Plot unsorted array
x = range(len(arr_test))
plt.plot(x, arr_test, marker='o')
plt.title("Unsortd array")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.show()

# Sort the array
merge_sort(arr_test)

# Plot sorted array
x = range(len(arr_test))
plt.plot(x, arr_test, marker='o')
plt.title("Sortd array")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.show()
