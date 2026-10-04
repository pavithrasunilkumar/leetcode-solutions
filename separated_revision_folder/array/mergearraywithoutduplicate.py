arr1 = [1, 2, 3, 4]
arr2 = [2, 3, 5, 6]


#method1 (TC = O(n+m) average	SC = O(n+m))
def merge_unique_set(arr1, arr2):
    return list(set(arr1 + arr2))

print(merge_unique_set(arr1, arr2))

#method2 (TC = O(n+m) 	SC = O(1))
def merge_unique(arr1, arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1

        elif arr2[j] < arr1[i]:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1

        else:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])

            i += 1
            j += 1
            

    while i < len(arr1):
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1

    while j < len(arr2):
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1

    return result


arr1 = [1, 2, 4, 5]
arr2 = [2, 3, 4, 6]

print(merge_unique(arr1, arr2))