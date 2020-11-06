# Homework 7
# Name: Serim Jang
# Andrew ID: serimj

import cs112_f17_week7_linter
import time, random, copy

##########

# Inverts the key and the value in the dictionary
def invertDictionary(d):
    dict = {}
    keyD = []
    valueD = []
    for key in d: # makes a list of inverted keys and values
        keyD += [d[key]]
        valueD += [key]
    for i in range(len(keyD)): # adds values to the dictionary
        if keyD[i] in dict: # if overlapping keys, adds to existing value
            dict[keyD[i]].add(valueD[i])
        else:
            dict[keyD[i]] = set([valueD[i]]) # changes list into a set
    return dict

# Finds a set of friends of friends that does not include the person, or
# friends of the person already
def friendsOfFriends(d):
    dict = {}
    friends = []
    for key in d: # person
        dict[key] = set()
        for friend in d[key]: # friend
            for fof in d.get(friend): # friend of friend
                # if not the person or the friends of the person
                if fof != key and fof not in d[key]:
                    dict[key].add(fof)
    return dict

def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])

def instrumentedSelectionSort(a):
    startTime = time.time()
    ncomp = 0
    nswap = 0
    n = len(a)
    for startIndex in range(n): # O(N)
        minIndex = startIndex
        for i in range(startIndex+1, n): # O(N)
            ncomp += 1
            if (a[i] < a[minIndex]):
                minIndex = i
        swap(a, startIndex, minIndex)
        nswap += 1
    endTime = time.time()
    # number of comparisons, number of swaps, time in seconds
    return (ncomp, nswap, endTime-startTime)

def instrumentedBubbleSort(a):
    startTime = time.time()
    ncomp = 0
    nswap = 0
    n = len(a)
    end = n
    swapped = True
    while (swapped):
        swapped = False
        for i in range(1, end): # O(N)
            ncomp += 1
            if (a[i-1] > a[i]): # O(N)
                swap(a, i-1, i)
                nswap += 1
                swapped = True
        end -= 1
    endTime = time.time()
    # number of comparisons, number of swaps, time in seconds
    return (ncomp, nswap, endTime-startTime)

def selectionSortVersusBubbleSort():
    a = [random.randint(0,2**31) for i in range(2**9)]
    copyA = copy.copy(a)
    selectionSortA = str(instrumentedSelectionSort(a))
    bubbleSortA = str(instrumentedBubbleSort(copyA))
    b = [random.randint(0,2**31) for i in range(2**10)]
    copyB = copy.copy(b)
    selectionSortB = str(instrumentedSelectionSort(b))
    bubbleSortB = str(instrumentedBubbleSort(copyB))
    c = [random.randint(0,2**31) for i in range(2**11)]
    copyC = copy.copy(c)
    selectionSortC = str(instrumentedSelectionSort(c))
    bubbleSortC = str(instrumentedBubbleSort(copyC))
    d = [random.randint(0,2**31) for i in range(2**12)]
    copyD = copy.copy(d)
    selectionSortD = str(instrumentedSelectionSort(d))
    bubbleSortD = str(instrumentedBubbleSort(copyD))
    print(selectionSortA, selectionSortB, selectionSortC, selectionSortD)
    print(bubbleSortA, bubbleSortB, bubbleSortC, bubbleSortD)
    print("We can see that, as N increases by two, the runtime increases by "\
    "four, as both selection sort and bubble sort is of O(N**2) efficiency.")
    print("Selection sort has more comparisons, runs in faster time, and has "\
    "less swaps than bubble sort.")

##### Test Functions #####

def testInvertDictionary():
    print("Testing invertDictionary()...", end="")
    assert(invertDictionary({1:2, 2:3, 3:4, 5:3}) == 
            {2:set([1]), 3:set([2,5]), 4:set([3])})
    assert(invertDictionary({1:5, 2:5, 3:5, 5:5}) == 
            {5:set([1,2,3,5])})
    assert(invertDictionary({1:2, 2:3, 3:4, 4:2, 5:3, 6:2}) == 
            {2:set([1,4,6]), 3:set([2,5]), 4:set([3])})
    print("Passed!")

def testFriendsOfFriends():
    print("Testing friendsOfFriends()...", end="")
    d = {}
    d["jon"] = set(["arya", "tyrion"])
    d["tyrion"] = set(["jon", "jaime", "pod"])
    d["arya"] = set(["jon"])
    d["jaime"] = set(["tyrion", "brienne"])
    d["brienne"] = set(["jaime", "pod"])
    d["pod"] = set(["tyrion", "brienne", "jaime"])
    d["ramsay"] = set()
    assert(friendsOfFriends(d) == 
    {'tyrion': {'arya', 'brienne'}, 
    'pod': {'jon'}, 
    'brienne': {'tyrion'}, 
    'arya': {'tyrion'}, 
    'jon': {'pod', 'jaime'}, 
    'jaime': {'pod', 'jon'}, 
    'ramsay': set()})
    print("Passed!")
    
#####  Test All & Main ####

def testAll():
    testInvertDictionary()
    testFriendsOfFriends()

def main():
    #cs112_f17_week7_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()