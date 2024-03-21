'''
This file is created for see the difference between David's code and mine
First run create_test_list program, be sure run same txt file
'''

ver_mine = []
ver_david = []

with open("test_file.txt", "r") as file:
    for line in file:
        word = line.rstrip()
        ver_mine.append(word)

with open("tolstoy.txt", "r") as file:
    for line in file:
        word = line.rstrip()
        ver_david.append(word)


print(f"output length: {len(ver_mine)} \nwishing lenght: {len(ver_david)}")
# input("press enter to continue")


longest = max(len(ver_mine), len(ver_david))
for i in range(longest):
    if ver_mine[i] != ver_david[i]:
        print(f"line {i+1}:\t{ver_mine[i]}\t{ver_david[i]}")
        # input("press enter to continue")

print("SUCCESS")
