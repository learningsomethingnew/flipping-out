
fib_seq_list = [1 ,2]
temp_num = 0

for i, number in enumerate(range(0, 4000000)):
    if temp_num < 3524578:
        temp_num = fib_seq_list[i] +fib_seq_list[i + 1]
        fib_seq_list.append(temp_num)
        print(fib_seq_list)

print(sum([x for x in fib_seq_list if x % 2 == 0]))

sum_list = []

############################################################
# Alternate solution
############################################################

values = [1, 2]
while values[-1] < 4000000:
    values.append(values[-1] + values[-2])






# for numb in fib_seq_list:
#     if numb %2 == 0:
#         sum_list.append(numb)
#         print("The number is {} and the sum_list is {}".format(numb, sum_list))
#         print(sum(sum_list))
