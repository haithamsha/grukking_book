#get the smallest number
#create new list
#put the small number in the new list one by one


def get_smallest_num(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = get_smallest_num(arr)
        newArr.append(arr[smallest])
    return newArr


arr_test = [5, 3, 2, 10]

print(selection_sort(arr_test))