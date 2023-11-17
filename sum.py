'''
Print the sum of the current number and the previous number
'''

previous_num = 0

for i in range(1,11):
    x_sum = previous_num + 1
    print("current number", i, "Previous number", previous_num, "sum", x_sum)
    previous_num = i