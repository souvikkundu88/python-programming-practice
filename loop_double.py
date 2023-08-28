'''
nums = [1, 3, 6, 10, 15, 21]

idx = 0

while idx < len(nums):
    num = nums[idx]
    print(num * num)
    idx += 1
'''



'''
float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
count_greater = 0

for num in float_list:  # Iterator traverses to the last index of the list
    if num > 10:
        count_greater += 1

print(count_greater)
'''
'''
string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
for s in string_list:
    if len(s) < 5:
        #print(len(s))
        print(s)
'''

def check_balance(brackets):
    check = 0
    for bracket in brackets:
        if bracket == '[':
            check += 1

        elif bracket == ']':
            check -= 1

    return check == 0


bracket_string = '[[[[]]'

print(check_balance(bracket_string))