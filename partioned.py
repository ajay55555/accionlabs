def partioned(tmp_list):
    for iter in tmp_list:
        yield iter

list_partioned = [1,2,3,4,5,6]

for item in partioned(list_partioned):
    print(item)