# Reeversing a string
# Input:  [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

# Constraint: Don't use arr.reverse() or arr[::-1]

arr = [1,2,3,4,5]
#using insert method

# result = []
# for i in arr:
#     result.insert(0,i)
# print(result)


#using two pointers
left = 0
right = len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print(arr)