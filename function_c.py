def merge_lists(list_a, list_b):
    for elem in list_a:
        list_b.append(elem)
    set_b = set(list_b)
    list_b=list(set_b)
    return list_b

print(merge_lists([1, 1, 2, 3], [3, 4, 5]))
