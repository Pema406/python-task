def multiply_lists(list1, list2):
    result = []
    for value1, value2 in zip(list1, list2):
        result. append(value1 * value2)
    list1 = [1,2,3,4,5]
    list2 = [4,4,3,2,1]
    print(multiply_lists(list1, list2)) # output:[5,8,9,8,5]