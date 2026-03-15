"""
Finds a target in a sorted list in O(log n) time.
Each step cuts the search space in half.
Linear search would need up to 1 million.
"""
def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    # prime numbers
    arr = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
           53, 59, 61, 67, 71, 73, 79, 83, 89, 97]    
    target = int(input(f"List: {arr}\nSearch for: "))
    index = binary_search(arr, target)

    if index != -1:
        print(f"Found {target} at index {index}.")
    else:
        print(f"{target} not in list.")