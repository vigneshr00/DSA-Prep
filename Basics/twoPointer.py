# 1. Check if a string is a palindrome, using two pointers (no slicing, no recursion this time).
def is_palindrome(k):
    left = 0
    right = len(k) - 1
    while left < right:
        if k[left] != k[right]:
            return False
        left += 1
        right -= 1
    return True

is_palindrome("racecar")
is_palindrome("mam")


# 2. Given a sorted array, find two numbers that add up to a target (like Two Sum, but exploit the fact it's sorted — no hashmap needed).
def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

two_sum_sorted([1,2,3,4,6], 6)

def remove_duplicates(arr):
    if not arr:
        return 0
    slow = 0   # tracks the position of the last unique element
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1

remove_duplicates([1,1,2,2,3])


def move_zeros(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
    return arr

move_zeros([0,1,0,3,12, 0, 17])

# 1. Given a sorted array, remove all instances of a given value in-place and return the new length.
def remove_element(arr, target):
    slow = 0
    for fast in range(len(sorted(arr))):
        if(arr[fast] != target):
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
    return slow, arr

remove_element([3,2,2,2,3,3], 2)   # returns 2, array becomes [2,2,...]

# 2. Given a sorted array of integers, return True if any two numbers are equal (i.e., contains a duplicate) — using two pointers, not a hashmap this time.
def has_duplicate_sorted(arr):
    slow = 0
    for fast in range(1, len(arr)):
        if(arr[slow] == arr[fast]):
            return True
        slow +=1
    return False


has_duplicate_sorted([1,2,3,4])   # True
has_duplicate_sorted([1,2,3,4])   # False


# 3. Given a string, check if it's a valid palindrome, ignoring non-alphanumeric characters and case.
def is_palindrome_clean(k):
    result = ""

    for char in k:
        if char.isalnum():
            result += char.lower()
    left = 0
    right = len(result) - 1
    while left < right:
        if result[left] != result[right]:
            return False
        left += 1
        right -= 1
    return True

is_palindrome_clean("A man, a plan, a canal: Panama")   # True
is_palindrome_clean("race a car")                        # False


# 4. Given an array of integers sorted in non-decreasing order, return the array of the squares of each number, also sorted in non-decreasing order — using two pointers (don't just square-then-sort).
def sorted_squares(arr):
    # slow = 0
    # fast = 1
    # while slow != len(arr):
    #     if(fast == len(arr)):
    #         slow += 1
    #         fast = slow + 1
    #     else: 
    #         if(abs(arr[slow]) > abs(arr[fast])):
    #             arr[slow], arr[fast] = arr[fast], arr[slow]
    #         fast += 1

    # return [x*x for x in arr]
    left = 0
    right = len(arr) - 1
    result = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        if(abs(arr[left]) > abs(arr[right])):
            result[i] = arr[left] ** 2
            left += 1
        else:
            result[i] = arr[right] ** 2
            right -= 1
    return result

sorted_squares([-4,-1,0,10, 13])   # [0,1,9,16,100]


# 5. Given two sorted arrays, merge them into one sorted array using two pointers (not + and sorted()).
def merge_sorted(arr1, arr2):
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if(arr1[i] <= arr2[j]):
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result
        
print(merge_sorted([1,3,5], [2,4,6]))   # [1,2,3,4,5,6]