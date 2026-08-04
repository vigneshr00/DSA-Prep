# --------------------------------------------------------- Day 1 -------------------------------------------------------------------

# Reeversing a string
# Input:  [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

# Constraint: Don't use arr.reverse() or arr[::-1]

#using insert method
def reverseArr(arr):
    result = []
    for i in arr:
        result.insert(0,i)
    return result

reverseArr([1,2,3,4,5])


#using two pointers
def twoPointer(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
twoPointer([1,2,3,4,5])



# -------------------------------------------------------------- Day 2 ----------------------------------------------------------------


# 1 Check if a string is a palindrome (reads the same forwards and backwards) — e.g., "madam" → True.


def palindrom(a):
    # using slicing
    # if(a == a[::-1]):
    #     print(True)

    # without using slicing
    b = ""
    for ch in a:
        b = ch + b

    if b == a:
        return True
    else:
        return False
palindrom("Vignesh")


# 2 Count the number of vowels in a given string.

vowels = ['a', 'e', 'i', 'o', 'u']
def countVowel(a):
    count = 0
    for ch in a:
        if(ch.lower() in vowels):
            count+=1
            
    return count

countVowel('aeiou')

# 3 Find the frequency of each character in a string (e.g., "hello" → {'h':1, 'e':1, 'l':2, 'o':1}).
def frequency(str):
    d1 = dict.fromkeys(list(str), 0)
    for i in str:
        d1[i] = d1[i]+1
    return d1
frequency("hello")  

# 4 Given an array [10, 20, 30, 40, 50], find the second largest element without using sorted() or max().

# not solved by myself
def second_largest(arr):
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second
second_largest([10,20,30,40])

# 5 Remove duplicate elements from an array while preserving order — e.g., [1,2,2,3,4,4,5] → [1,2,3,4,5].

def removeDup(arr):
    res = []
    for i in arr:
        if(i not in res):
            res.append(i)
    return res

removeDup([1,2,2,3,4,4,5])

# 6 Check if two strings are anagrams of each other (e.g., "listen" and "silent").

def anagram(a,b):
    arr1 = sorted(list(a))
    arr2 = sorted(list(b))
    if(arr1 == arr2 ):
        return True
    else:
        return False
anagram("listen","silent")

# 7 Find the first non-repeating character in a string — e.g., "swiss" → 'w'.
# def firstNonRepeating(str):
#     res = ''
#     for i in range(len(str)):
#         str1 = str[i+1:]
#         if(str[i] not in str1):
#             res = str[i]
#             break
#     return res
def firstNonRepeating(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return s[i]
    return None
firstNonRepeating("teeter")

# Try a few and share your code — I'll review it and point out what's working well and what could be cleaner.


# --------------------------------------------------- Day 3 ------------------------------------------------------------------

# 1. Given a list of words, count the frequency of each word.
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# Expected: {'apple': 3, 'banana': 2, 'cherry': 1}

def count_frequescy(arr):
    result = {}
    for i in arr:
        if(i in result):
            result[i] += 1
        result.setdefault(i, 1)
    return result
count_frequescy(words)


# 2. Given two dictionaries, merge them. If a key exists in both, sum their values.
# d1 = {"a": 10, "b": 20, "c": 30}
# d2 = {"b": 5, "c": 10, "d": 40}
# Expected: {'a': 10, 'b': 25, 'c': 40, 'd': 40}

def merginDict(d1, d2):
    for key, value in d2.items():
        if(key in d1):
            d1[key] = d1[key] + value
        else:
            d1[key] = value
    return d1
merginDict({"a": 10, "b": 20, "c": 30},{"b": 5, "c": 10, "d": 40})

#3. Find the key with the maximum value in a dictionary (without using max()).
scores = {"Alex": 85, "Priya": 92, "John": 78}
# Expected: 'Priya'

def findMaxKey(d1):
    maxValue = 0
    maxKey = ""
    for key, value in d1.items():
        if(maxValue < value):
            maxValue = value
            maxKey = key
    return maxKey

findMaxKey(scores)


# 4. Invert a dictionary (swap keys and values).
d = {"a": 1, "b": 2, "c": 3}
# Expected: {1: 'a', 2: 'b', 3: 'c'}

def invertDict(d1):
    d2 = {}
    for key, value in d1.items():
        d2[value] = key
    return d2

invertDict(d)

# 5. Given a 2D array (list of lists), find the sum of all elements.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Expected: 45
def sumOfAllElements(d1):
    result = 0
    for i in d1:
        for j in i:
            result += j
    return result

sumOfAllElements(matrix)


# 6. Print a 2D array in transposed form (rows become columns).
matrix = [[1, 2, 3], [4, 5, 6]]
# Expected: [[1, 4], [2, 5], [3, 6]]

def twoDArr(arr):
    arr1 = [[] for _ in range(len(arr[0]))]
    for i in arr:
        for j in i:
            arr1[i.index(j)].append(j)
    return arr1
twoDArr(matrix)

#7. Given a 2D array, find the row with the maximum sum.
matrix = [[1, 2, 3], [10, 20, 30], [4, 5, 6]]
# Expected: index 1 (sum = 60)
def maxArr(arr):
    max = 0
    maxIndex = 0
    result = ''
    for i in arr:
        total = 0
        for j in i:
            total += j
        if(max < total):
            max = total
            maxIndex = arr.index(i)
    return f"index {maxIndex} (sum = {max})"
maxArr(matrix)



#8. Print all elements of a 2D array in a diagonal pattern (top-left to bottom-right).
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Expected: [1, 5, 9]

def diagonalPattern(arr):
    result = []
    for i in arr:
        result.append(i[arr.index(i)])
    return result

diagonalPattern(matrix)

# ------------------------------ Day 4 -------------------------------------

# 1. Write a recursive function to calculate the factorial of a number.

def factorial(n):
    if n == 0:
        return 1
    return n* factorial(n-1)

factorial(5)

# 2. Write a recursive function to calculate the sum of the first n natural numbers.

def sumOfNaturalNumbers(n):
    if n == 0:
        return 0
    return n + sumOfNaturalNumbers(n-1)

sumOfNaturalNumbers(5)

# 3. Write a recursive function to find the nth Fibonacci number

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(6)

# 4. Write a recursive function to reverse a string (no slicing, no loops — recursion only).

def reverse_str(string, index=None):
    if index is None:
        index = len(string) - 1

    if index < 0:
        return ""

    return string[index] + reverse_str(string, index - 1)

reverse_str("hello")

# 5. Write a recursive function to check if a string is a palindrome.

def is_palindrome(value, result):
    if len(value) == 1:
        return result
    if(value[0] == value[-1] and len(value) > 2):        
        return is_palindrome(value[1:-1], True)
    elif len(value) == 2 and value[0] == value[-1]:
        return True
    else:
        return False

is_palindrome("madam", False)   # Expected: True
is_palindrome("absfba", False)   # Expected: False


# 6. Write a recursive function to find the maximum element in a list (no max()).

# find_max([3, 7, 2, 9, 4])   # Expected: 9

def find_max(arr, result):
        if len(arr) == 0:
            # print("first.....",arr, result)
            return result
        if arr[0] > result:
            # print("second.....",arr, result)
            return find_max(arr[1:], arr[0])
        else:
            return find_max(arr[1:], result)

# this version is given by chatgpt

    #     def find_max(arr):
    # if len(arr) == 1:
    #     return arr[0]

    # max_rest = find_max(arr[1:])

    # if arr[0] > max_rest:
    #     return arr[0]
    # else:
    #     return max_rest


# print(find_max([90, 1, 2, 70, 5, 10]))

print(find_max([-5, -2, -8], float("-inf") ))
    

# 7. Write a recursive function to calculate x raised to the power n (i.e., x^n).

# power(2, 5)   # Expected: 32
def power(x, n):
    if n == 0:
        return 1
    return x * power(x , n-1)

power(5,2)


# 8. Write a recursive function to count the number of digits in a number.

def count_digits(arr, result):
        if arr // 10 == 0:
            return result+1
        else:
            return count_digits(arr // 10,result = result+1 )
count_digits(12345, 0)   # Expected: 5