import random
import time

class QuickSort:
    def __init__(self, arr, order="asc"):
        self.arr = arr
        self.order = order  # "asc" for ascending, "desc" for descending

    def randomized_quicksort(self, low, high):
        if low < high:  # Ensure we have more than one element to sort
            pivot_index = self.randomized_partition(low, high)
            self.randomized_quicksort(low, pivot_index - 1)  # Sort left part
            self.randomized_quicksort(pivot_index + 1, high)  # Sort right part

    def randomized_partition(self, low, high):
        pivot_index = random.randint(low, high)  # Choose a random pivot index from low to high
        self.arr[pivot_index], self.arr[high] = self.arr[high], self.arr[pivot_index]  # Swap pivot to end
        return self.partition(low, high)

    def partition(self, low, high):
        pivot = self.arr[high]  # Use the last element as pivot
        i = low - 1  # Pointer for the smaller element
        for j in range(low, high):  # Traverse through all elements
            # Comparison condition based on order
            if (self.order == "asc" and self.arr[j] <= pivot) or (self.order == "desc" and self.arr[j] >= pivot):
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]  # Swap
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]  # Swap pivot to correct position
        return i + 1  # Return the pivot index

    def measure_time(self):
        start_time = time.time()
        self.randomized_quicksort(0, len(self.arr) - 1)
        end_time = time.time()
        return end_time - start_time

def get_user_input():
    choice = input("Choose the type of array:\n1. Input your own array\n2. Random array\n3. Sorted array\nEnter your choice (1-3): ")
    if choice == '1':
        arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    elif choice == '2':
        size = int(input("Enter the size of the random array: "))
        arr = [random.randint(0, 10000) for _ in range(size)]
    elif choice == '3':
        size = int(input("Enter the size of the sorted array: "))
        arr = list(range(size))  # Sorted array
    else:
        print("Invalid choice")
    return arr

def main():
    arr = get_user_input()
    print("Original Array:", arr)

    # Sort in ascending order
    qs_asc = QuickSort(arr.copy(), order="asc")
    time_taken_asc = qs_asc.measure_time()
    print("Sorted Array (Ascending):", qs_asc.arr)
    print(f"Time taken (Ascending): {time_taken_asc:.6f} seconds")

    # Sort in descending order
    qs_desc = QuickSort(arr.copy(), order="desc")
    time_taken_desc = qs_desc.measure_time()
    print("Sorted Array (Descending):", qs_desc.arr)
    print(f"Time taken (Descending): {time_taken_desc:.6f} seconds")

# Run the main function
main()