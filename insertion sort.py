def insertion_sort(arr):
    """
    Function to perform insertion sort on a given list.
    
    Parameters:
    arr (list): The list to be sorted.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    # Example usage
    unsorted_list = [64, 25, 12, 22, 31]
    print("Unsorted List:", unsorted_list)

    # Call the insertion_sort function to sort the list
    insertion_sort(unsorted_list)

    print("Sorted List:", unsorted_list)

if __name__ == "__main__":
    main()
