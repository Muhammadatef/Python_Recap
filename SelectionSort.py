def smallest_element(arr):
    smallest_element = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest_element:
            smallest_element= arr[i]
            smallest_index = i
    return smallest_index


# print(f"smallest index  and its value perspective are {smallest_element([5,4,3,42,44,2])}")

def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = smallest_element(arr)
        newArr.append(arr.pop(smallest))
    return newArr

arr1=[10,8,77,8,88,9,2]
print(f"selection Sort for this {arr1} is {selection_sort(arr1)}")
