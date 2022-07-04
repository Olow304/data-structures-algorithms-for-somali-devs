def mergeTwoSortedArrays(arr1, arr2) -> []:
    """
    We loop through both arrays, comparing the first element of each array. We append the smaller
    element to our output array, and increment the index of the array from which we took the element. We
    repeat this process until we have exhausted one of the arrays, at which point we append every
    remaining element in the non-exhausted array to our output array
    
    :param arr1: [1, 3, 5, 7]
    :param arr2: [2, 4, 6, 8]
    :return: [1, 2, 3, 4, 5, 6, 7, 8]
    """
    output = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            output.append(arr1[i])
            i += 1
        else:
            output.append(arr2[j])
            j += 1

    while i < len(arr1):
        output.append(arr1[i])
        i += 1

    while j < len(arr2):
        output.append(arr2[j])
        j += 1

    return output


arr1 = [1,3,5,7]
arr2 = [2,4,6,8]

print(mergeTwoSortedArrays(arr1, arr2)) # -> [1, 2, 3, 4, 5, 6, 7, 8]