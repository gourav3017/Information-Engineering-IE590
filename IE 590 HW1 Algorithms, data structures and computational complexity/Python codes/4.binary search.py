from numpy import *

# Test array
arr = [2,3,4,5,6,10,30,35,40,50,70,90] #accept input as array
print(arr)
x=int(input("Enter the value to be searched in given array:")) #Value to be searched
high=len(arr)
def binarySearch(arr, l, high, x):
    while l <= high:

        mid = round(l + (high - l) / 2);

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index",result)
else:
    print("Element is not present in array")