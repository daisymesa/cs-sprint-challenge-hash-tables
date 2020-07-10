'''
Find the intersection between multiple lists of integers.

Do not use numpy or sets to solve this; use dict or hashtables, please.

We're given a list of lists that contain integers:

[
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
]
And we need to compute the intersection, that is, numbers that exist in all lists.

From the above input, the return value will be:

[1, 2]
Because those are the numbers that exist in all the lists.

(Output can be in any order.)

Limits:

There can be up to 10 lists in the list of lists.
The lists can contain up to roughly 1,000,000 elements each.
'''


def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # creating empty dict for integers in arrays
    nums_dict = {}
    # creating result to return in the end
    result = []

    # add nums to empty nums_dict with 0 for initial values
    for array in arrays:
        for num in array:
            nums_dict[num] = 0

    # in each nums_dict, if there is a match with array nums, increase the value of that num in nums_dict by 1
    for array in arrays:
        for num in array:
            if num in nums_dict:
                nums_dict[num] += 1

    # loop through nums_dict, if any nums value == the number of total arrays, then we have a match
    for key, value in nums_dict.items():
        # if we have a match, then append that num (the key) to the result
        if value == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))


# test_arr = [
#     [1, 2, 3, 4, 5],
#     [12, 7, 2, 9, 1],
#     [99, 2, 7, 1,]
# ]

# print(intersection(test_arr))
