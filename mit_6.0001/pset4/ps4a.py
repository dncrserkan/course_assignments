def get_permutations(sequence):
    if len(sequence) == 1:
        return [sequence]
    result =[]
    for i in range(len(sequence)):
        char = sequence[i]
        left_sequence = sequence[:i] + sequence[i+1:]
        loop = get_permutations(left_sequence)
        for j in loop:
            result += [char+j]      # j is string not a list
    
    # to remove duplicates first change list to dictionary then change to list
    result = list(dict.fromkeys(result))    
    return result


def test_get_permutations(expected_output, actual_output):
    if len(expected_output) == len(actual_output):
        for item in expected_output:
            if item not in actual_output:
                print("At least one elements doesn't exist in your list...")
        print("Test success...")
    else:
        if len(expected_output) > len(actual_output):
            print("Your list has fewer element than we expect...")
        else:
            print("Your list has more elements than we expect...")
    input('press enter to continue')


    
if __name__ == '__main__':
    #EXAMPLES
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print('- '* 10)
    
    example_1 = 'bug'
    expect_1 = ['bug', 'bgu', 'ubg', 'ugb', 'gbu', 'gub']
    actual_1 = get_permutations(example_1)
    print('Input:', example_1)
    print('Expected Output', expect_1)
    print('Actual Output', actual_1)
    test_get_permutations(expect_1, actual_1)
    print('- ' * 10)
    
    example_2 = 'lol'
    expect_2 = ['lol', 'llo','oll']
    actual_2 = get_permutations(example_2)
    print('Input:', example_2)
    print('Expected Output', expect_2)
    print('Actual Output', actual_2)
    test_get_permutations(expect_2, actual_2)
    print('- ' * 10)
    
    example_3 = 'zen'
    expect_3 = ['zen', 'zne', 'ezn', 'enz', 'nez', 'nze']
    actual_3 = get_permutations(example_3)
    print('Input:', example_3)
    print('Expected Output', expect_3)
    print('Actual Output', actual_3)
    test_get_permutations(expect_3, actual_3)
    print('- ' * 10)

    example_4 = 'bb'
    expect_4 = ['bb']
    actual_4 = get_permutations(example_4)
    print('Input:', example_4)
    print('Expected Output', expect_4)
    print('Actual Output', actual_4)
    test_get_permutations(expect_4, actual_4)
    print('- ' * 10)

    example_5 = 'abcd'
    expect_5 = ['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 
                'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca',
                'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba',
                'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba',
                ]
    actual_5 = get_permutations(example_5)
    print('Input:', example_5)
    print('Expected Output', expect_5)
    print('Actual Output', actual_5)
    test_get_permutations(expect_5, actual_5)
    print('- ' * 10)
 