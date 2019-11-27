# Implement a merge sort with recursion


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53] # list

def mergesort(dataset): 
    if len(dataset) > 1: # This is the breaking condition
        mid = len(dataset) // 2 # fine mid point of array/list (!) '//' is floor division -> result is quotient in which decimals are removed and floored
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # TODO: recursively break down the arrays
        mergesort(leftarr)
        mergesort(rightarr)

        # TODO: now perform the merging
        i=0 # index into the left array
        j=0 # index into the right array
        k=0 # index into merged array

        # TODO: while both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        # TODO: if the left array still has values, add them
        while i < len(leftarr):
            dataset[k] = leftarr[i] # already sorted at this pont
            i += 1
            k += 1

        # TODO: if the right array still has values, add them
        while j < len(rightarr):
                dataset[k] = rightarr[j]
                j += 1
                k += 1


# test the merge sort with data
print(items)
mergesort(items)
print(items)

