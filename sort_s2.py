
def bubble_sort(a, n: int) -> None:
    
    for i in range(n - 1, 0, -1): 
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def selection_sort(a, n: int) -> None:
    
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[min_idx], a[i] = a[i], a[min_idx]


def merge_sort(a, n: int) -> None:
    #check if list size smaller than 2
    if n <= 1:
        return
    #find middle of list to split
    mid = n // 2
    left = a[:mid]
    right = a[mid:]

    merge_sort(left, len(left))
    merge_sort(right, len(right))

    i = j = k = 0
    # compare left and right list and add the smallest to a
    while i < len(left) and j < len(right):
        if left[i] < right[j]:  
            a[k] = left[i]      
            i += 1               
        else:
            a[k] = right[j]
            j += 1
        k += 1                   
    # if the cuurent counter i hasn't parsed over all the items in left list then just add them to a
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    # if the cuurent counter j hasn't parsed over all the items in right list then just add them to a
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1
    


def insertion_sort(a, n: int) -> None:
    
    for i in range(1, n):
        elem = a[i]
        j = i-1

        # Search for the location j where we'll insert element a[i]
        # while shifting the elements stored in a[j] .. a[i-1] to the right,
        # to make room for a[i]

        while j >= 0 and a[j] > elem:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = elem


def heapsort(a, n: int) -> None:
    
    for i in range(n // 2 - 1, -1, -1):
        trickle_down(a, i, n)

    # Sort a[0] .. a[n - 1] into descending order.

    i = n
    while i > 1:
        i -= 1
        # Remove the smallest element from the heap (located at (at a[0])
        # by swapping it and the rightmost child on the lowest level.
        a[i], a[0] = a[0], a[i]

        # Treat a[0] .. a[i-1] as a heap, except the root element may not be
        # in the correct position.
        # Reform a[0] .. a[i-1] into a heap, by trickling the root element
        # down the heap's tree until the heap property has been restored.
        trickle_down(a, 0, i)

        # Now, a[0] .. a[i-1] is a min heap, and a[i] .. a[n - 1]
        # contains the elements that were removed from the heap, sorted in
        # descending order.

    # Rearrange a's elements into ascending order.
    reverse(a, n)


# For a detailed description of the trickle-down algorithm,
# see method _trickle_down in class BinaryHeap.


def trickle_down(a, i: int, n: int) -> None:
    """Starting with the element stored at index i in the heap's array,
    trickle this element down the tree until the heap has been reformed.

    The heap has n elements.
    """
    # Repeatedly swap the element at index i with its smallest child,
    # until the element is no longer larger than its children.

    while i >= 0:
        j = -1
        r = right(i)
        if r < n and a[r] < a[i]:
            l = left(i)
            if a[l] < a[r]:
                j = l
            else:
                j = r
        else:
            l = left(i)
            if l < n and a[l] < a[i]:
                j = l

        if j >= 0:
            a[j], a[i] = a[i], a[j]
        i = j


def left(i: int) -> int:
    """Return the index of the left child of the node at index i in the array.
    """
    return 2 * i + 1


def right(i: int) -> int:
    """Return the index of the right child of the node at index i in the array.
    """
    return 2 * (i + 1)


def parent(i: int) -> int:
    """Return the index of the parent of the node at index i in the array."""
    return (i - 1) // 2


def reverse(a, n):
    """Reverse the first n elements of sequence a in place."""
    for i in range(n // 2):
        a[i], a[n - 1 - i] = a[n - 1 - i], a[i]


