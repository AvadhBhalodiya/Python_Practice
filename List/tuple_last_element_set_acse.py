l1 = [(2,4), (3,3), (1,2)]

def Sort_Tuple(l1):

    l = len(l1)

    for i in range(0, l):
        for j in  range(0, l-i-1):
            if( l1[j][-1] > l1[j+1][-1]):
                temp = l1[j]
                l1[j] = l1[j+1]
                l1[j+1] = temp
    return l1


print("Sorting = ", Sort_Tuple(l1))