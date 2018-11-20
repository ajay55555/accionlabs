def find_equal_sum(lst):
    lenght = len(lst)
    total_sum=(lst)
    temp_sum = 0
    for i in range(lenght-1,-1,-1):
        temp_sum += lst[i]
        total_sum -= lst[i]

        if total_sum == temp_sum:
            print("possible to divide")
            return i
    return -1

call_list = [1,2,3,4,5,5]
data = find_equal_sum(call_list)
print(data)

if data == -1:
    print("partion not possible")
else:
    print(call_list[:data], "and", call_list[data:])