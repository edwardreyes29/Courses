items = [6, 20, 8, 19, 49, 22, 532, 55, 22]

def mergesort(dataset):
    if len(dataset) > 1: # This breaks condition
        mid = len(dataset) // 2 # floor division
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # recursively break down arrays
        mergesort(leftarr)
        mergesort(rightarr)

        i = 0 # index into left array
        j = 0 # index into right array
        k = 0 # index into merged array

        # TODO: while both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        # if left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1
        # if right array still has values, add them
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1

print(items)
mergesort(items)
print(items)