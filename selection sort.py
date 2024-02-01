def selection_sort(arr):
    """
    Function to perform selection sort on a given list.
    
    Parameters:
    arr (list): The list to be sorted.
    """
    n = len(arr)
    
    for i in range(n-1):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

def main():
    # Example usage
    unsorted_list = [64, 25, 12, 22, 31]
    print("Unsorted List:", unsorted_list)

    # Call the selection_sort function to sort the list
    selection_sort(unsorted_list)

    print("Sorted List:", unsorted_list)

if __name__ == "__main__":
    main()
