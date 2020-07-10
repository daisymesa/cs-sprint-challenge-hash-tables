def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # making empty dict for numbers
    num_dict = {}
    # making empty result variable for output
    result = []

    # loop each number in a
    for num in a:
        # check if there is another instance of num, positive or negative
        # if positive + negative add to 0, we have a match
        if num_dict.get(abs(num)) and num_dict.get(abs(num)) + num == 0:
            # if yes, append to final results
            result.append(abs(num))
        else:
            # else add key with num as its value
            num_dict[abs(num)] = num

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))  # output: [1, 2, 4]
