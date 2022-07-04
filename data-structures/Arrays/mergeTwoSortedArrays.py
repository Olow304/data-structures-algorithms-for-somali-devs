"""
    Let's assume that we have two sorted array and we would like to merge both arrays

    arr1 = [1,3,5,7]
    arr2 = [2,4,6,8]

    output = [1,2,3,4,5,6,7,8]
"""

def mergeTwoSortedArrays(arr1, arr2):
    # we want to loop through both arrays
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