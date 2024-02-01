def merge_sort(arr):
    """
    Function to perform merge sort on a given list.
    
    Parameters:
    arr (list): The list to be sorted.
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the list
        left_half = arr[:mid]  # Divide the list into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursive call on the left half
        merge_sort(right_half)  # Recursive call on the right half

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in both halves
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def main():
    # Example usage
    unsorted_list = [64, 25, 12, 22, 11]
    print("Unsorted List:", unsorted_list)

    # Call the merge_sort function to sort the list
    merge_sort(unsorted_list)

    print("Sorted List:", unsorted_list)

if __name__ == "__main__":
    main()
