# searching for an item in an ordered list
# this technique uses a binary search


items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarysearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    # As long as indexes don't cross over each other
    while lowerIdx <= upperIdx:
        # TODO: calculate the middle point
        midPt = (lowerIdx + upperIdx) // 2
        # print("The midpoint is {}".format(midPt))
        # TODO: if item is found, return the index
        if itemlist[lowerIdx] == item:
            return lowerIdx
        if itemlist[midPt] == item:
            return midPt
        if itemlist[upperIdx] == item:
            return upperIdx


        # TODO: otherwise get the next midpoint
        if item > itemlist[midPt]:
            lowerIdx = midPt + 1
        else: 
            upperIdx = midPt - 1

    if lowerIdx > upperIdx:
        return None

print(binarysearch(6, items))
print(binarysearch(23, items))
print(binarysearch(87, items))
print(binarysearch(250, items))
