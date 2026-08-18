# 1. Contains Duplicate — solve both brute force (nested loop) and optimized (set-based).

def contains_duplicate(arr):
    seen = set()
    if(len(arr) < 2):
        return False
    for i in arr:
        if(i in seen):
            return True
        seen.add(i)
    return False

contains_duplicate([1,2,3,4,4])   # True
contains_duplicate([1,2,2])   # False

# 2. Anagram check using character counts (dictionary), not sorting.

def is_anagram(a, b):
    dict1 = {}
    dict2 = {}
    for i in a:
        dict1[i] = dict1.setdefault(i, 0) + 1
    
    for i in b:
        dict2[i] = dict2.setdefault(i, 0) + 1

    return dict1 == dict2
    

is_anagram("listen", "silent")   # True
is_anagram("hello", "world")     # False



# 3. Two Sum — return indices of the two numbers that add up to target, using the complement pattern.

def two_sum(arr, target):
    seen = {}
    for i in range(len(arr)):
        difference = target - arr[i]
        if(difference in seen):
            return [seen[difference] , i]
        seen[arr[i]] = i
    return []

two_sum([3,2,4], 6)   # [1, 2]



# 4. Intersection of two arrays — elements in both, no duplicates in result.

def intersection(arr1, arr2):
    result = []
    there = {}
    for i in range(len(arr2)):
        if(arr2[i] in arr1):
            there[arr2[i]] = 1
    for i in there.keys():
        result.append(i)
    return result

print(intersection([1, 2, 2, 1], [1, 2]))   # [2]


# 5. First unique character in a string, using a dictionary/Counter approach.

def first_unique_char(a):
    for i in range(len(a)):
        s = a[:i] + a[i + 1:]
        if(a[i] not in s):
           return a[i]
        
    return None

first_unique_char("")   # 'w'

