
test_list = [0, 1, 3, 4, 6, 7, 8, 1, 2, 4, 5, 7, 0, 1, 2, 4, 3, 5, 6, 8, 6]

test_dict = {}
conversation=dict(aphone='recording')

for num in test_list:
    if num not in test_dict:
        test_dict[num] = 1
    else:
        test_dict[num] += 1


print(conversation)
