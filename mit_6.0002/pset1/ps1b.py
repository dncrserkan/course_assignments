###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators: 
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """

    current = (lambda d: sum(key * d[key] for key in d))(memo)
    available = target_weight - current

    if available == 0:
        # print(memo, available, egg_weights)
        return sum(memo.values())
    
    if egg_weights[-1] <= available:
        # print(memo, available, egg_weights)
        memo[egg_weights[-1]] = memo.get(egg_weights[-1], 0) + 1
        return dp_make_weight(egg_weights, target_weight, memo)
    
    else:
        # print(memo, available, egg_weights)
        return dp_make_weight(egg_weights[:-1], target_weight, memo)


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    print()
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()

    # egg_weights_2 = (1, 5, 10, 20)
    # n_2 = 99
    # print("Egg weights = (1, 5, 10, 20)")
    # print("n = 99")
    # print("Expected ouput: 10 (4 * 20 + 1 * 10 + 1 * 5 + 4 * 1 = 99)")
    # print("Actual output:", dp_make_weight(egg_weights_2, n_2))
    # print()

    # egg_weights_3 = (1, 5, 10, 20)
    # n_3 = 6
    # print("Egg weights = (1, 5, 10, 20)")
    # print("n = 6")
    # print("Expected ouput: 2 (1 * 5 + 1 * 1 = 6)")
    # print("Actual output:", dp_make_weight(egg_weights_3, n_3))
    # print()
