best = [1]
in_order = [1, 2, 3]
out_order = [3, 1, 2]
worst = [3, 2, 1]

def bubble_sort(arr):

    # Get length of array
    n = len(arr)

    # Runtime counter
    total = 0

    # Iterate through entire array
    for i in range(n):
        total+=1
        # Iterate through the higher portion of the array as the array size shrinks
        for j in range( (n-i) - 1 ):
            
            total+=1

            # Swap if lower index contains a higher value
            if arr[j] > arr[j+1]:
                total+=1
                # Temporary holder for smaller value
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            print(arr)
    print(n)
    print(total)


bubble_sort(out_order)