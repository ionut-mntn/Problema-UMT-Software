# Mathematical reasoning:
# First, let us consider:
# arr - the given array
# A, B - the 2 partitions(arrays) in the hypothesis
# sum_X - sum of the elements in the array X
# len_X - number of elements in the array X
#
# Based on the hypothesis, we know:
# 1) sum_A + sum_B = sum_arr
# 2) len_A + len_B = len_arr
#
# We have to determine if:
# sum_A / len_A = sum_B / len_B (the partitions have the same average)

# If we substitute sum_B, len_B -with regards to the given array - we can rewrite the above equation as:
# sum_A / len_A = (sum_arr - sum_A) / (len_arr - len_A) <=>
# <=> sum_A * (len_arr - len_A) = len_A * (sum_arr - sum_A) <=>
# <=> sum_A * len_arr - sum_A * len_A = sum_arr * len_A - sum_A * len_A    # here we add sum_A * len_A to both parts of the equation
# <=> sum_A * len_arr = sum_arr * len_A

# The last obtained equation we wrote could be written as:
# sum_A = len_A * sum_arr / len_arr

# Given this equation that we end up with, we can state that:
# in order for two partitions of the given array to exist so that they have the same average, then:
# the sum of the elements in any of the partitions - let us call this partition X - should be equal to:
# len_partition_X * sum_arr / len_arr

# Therefore, we will be iterating and check if this is possible for partitions of length [1 ... int(len_arr/2)]
# The reason we are checking only up to int(len_arr/2) is because we know one of our partitions has to be less than or equal to
# the length of the given array divided by two

# However, for len_arr = 2 we will have to manually check, because len_arr/2 would be 1 and the mathematical statement:
# (sum_arr * i) % (len_arr/2) would be valid for any value of i. This will represent an edge case we will handle in the
# function



# 'given_arr' parameter will represent a list of integers corresponding to the integer array described in the problem
def check_split_list_same_average(given_arr):

    dim = len(given_arr)
    if dim < 2:
        return False
    if dim == 2:
        return given_arr[0] == given_arr[1]

    summ = sum(given_arr)
    half_dim = dim // 2

    for i in range(1,half_dim + 1):
        if summ * i % dim == 0:
            return True
    return False

if __name__ == '__main__':

    print('1) ', [1,10], check_split_list_same_average([1,10]))                      # should print False
    print('2) ', [2,4,5,7,10,14], check_split_list_same_average([2,4,5,7,10,14]))             # should print True
    print('3) ', [1,2,3,4,5,6,7,8], check_split_list_same_average([1,2,3,4,5,6,7,8]))           # should print True
    print('4) ', [7, 9], check_split_list_same_average([7, 9]))                      # should print False
    print('4) ', [8, 11, 12], check_split_list_same_average([8, 11, 12]))                 # should print False
    print('4) ', [8, 10, 12], check_split_list_same_average([8, 10, 12]))                 # should print True
    print('5) ', [1, 5, 7, 2, 0], check_split_list_same_average([1, 5, 7, 2, 0]))             # should print True
    print('6) ', [4, 3, 5, 9, 11], check_split_list_same_average([4, 3, 5, 9, 11]))            # should print False
    print('7) ', [1,2,3,4,5,6,7,8,9,10], check_split_list_same_average([1,2,3,4,5,6,7,8,9,10]))      # should print True