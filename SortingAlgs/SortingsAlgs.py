def bubbleSortASC(arr):
    
    n = len(arr)

    # For loop to traverse through all 
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):
            
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found 
            #is greater than the adjacent element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def bubbleSortDESC(arr):
    
    n = len(arr)

    # For loop to traverse through all 
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):
            
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found 
            #is greater than the adjacent element
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selectionSortASC(arr):
    size = len(arr)

    for s in range(size):
        min_idx = s
        
        for i in range(s + 1, size):
            
            # For sorting in descending order
            # for minimum element in each loop
            if arr[i] < arr[min_idx]:
                min_idx = i

        # Arranging min at the correct position
        (arr[s], arr[min_idx]) = (arr[min_idx], arr[s])
    return arr

def selectionSortDESC(arr):
    size = len(arr)
    
    for s in range(size):
        min_idx = s
        
        for i in range(s + 1, size):
            
            # For sorting in descending order
            # for minimum element in each loop
            if arr[i] > arr[min_idx]:
                min_idx = i

        # Arranging min at the correct position
        (arr[s], arr[min_idx]) = (arr[min_idx], arr[s])
    return arr

def insertionSortASC(arr): 
  
        # Outer loop to traverse on len(arr)  
        for i in range(1, len(arr)):  
  
            a = arr[i]  
  
            # Move elements of arr[0 to i-1], 
            # which are greater to one position
            # ahead of their current position  
            j = i - 1  
          
            while j >= 0 and a < arr[j]:  
                arr[j + 1] = arr[j]  
                j -= 1  
                
            arr[j + 1] = a  
            
        return arr 

def insertionSortDESC(arr):
    
        # Outer loop to traverse on len(arr)  
        for i in range(1, len(arr)):  
  
            a = arr[i]  
  
            # Move elements of arr[0 to i-1], 
            # which are greater to one position
            # ahead of their current position  
            j = i - 1  
          
            while j <= 0 and a > arr[j]:  
                arr[j + 1] = arr[j]  
                j -= 1  
                
            arr[j + 1] = a  
            
        return arr 

def is_sortedDESC(arr):
    """
    Check if the array is sorted in DESCENDING order.

    Args:
        arr (list): The array to check.

    Returns:
        bool: True if the array is sorted, False otherwise.
    """
    return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

def is_sortedASC(arr):
    """
    Check if the array is sorted in ASCENDING order.

    Args:
        arr (list): The array to check.

    Returns:
        bool: True if the array is sorted, False otherwise.
    """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
# Driver code

# Example to test the above code
arr = [ 2, 1, 10, 23 ]

print(arr)
print(is_sortedDESC(arr))

print(insertionSortDESC(arr))

print(is_sortedDESC(arr))

