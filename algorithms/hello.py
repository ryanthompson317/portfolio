from termcolor import colored

print(colored("hello bob", "cyan"))

x = [42, 7, 7, 2, 5, 0, -1, 16]


def bubble_sort(in_arr):
    
    n = len(in_arr)

    for i in range(n):
        for j in range(0, n - 1 - i):

            if in_arr[j] > in_arr[j + 1]:
                # in_arr[j], in_arr[j + 1] = in_arr[j + 1], in_arr[j]
                temp = in_arr[j]
                in_arr[j] = in_arr[j+1]
                in_arr[j + 1] = temp            
                                
                print(str(i) + "." + str(j))
            print(in_arr)

def insertionSort(in_arr):

    n = len(in_arr)

    for i in range(1, n):
        key = in_arr[i]

        j = i-1
        while j >= 0 and key < in_arr[j]:
            in_arr[j+1] = in_arr[j]
            j -= 1
        in_arr[j+1] = key
        print(str(i) + "." + str(j+1))
        print(in_arr)


# bubble_sort(x)
insertionSort(x)
# print(x)