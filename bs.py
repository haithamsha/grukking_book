import pytest
#Binary search
# low = 0
# hight = len(list) -1 
# mid = (low + high) / 2  , result = mid
# while low <= high       if input < result then hight = mid  - 1
#                         if input > result then low = mid + 1


def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    

    while low <= high:
        mid = (low + high) // 2
        result = arr[mid]

        if item == result:
            return mid
        if item < result:
            high = mid -1
        else:
            low = mid +1
    return "Not Found"


def test_binary_search_notfound():
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, -1) == "Not Found"

def test_binary_search_first_time():
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 5) == 2

def test_binary_search_last():
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 9) == 4

            
arr = [1, 3, 5, 7, 9]
print(binary_search(arr, 9))
