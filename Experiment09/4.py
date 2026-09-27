def merge_sorted_lists(list1, list2):

    merged_list = list1 + list2
    merged_list.sort()
    return merged_list


list_a = [3, 1, 4]
list_b = [2, 5, 0]
print(merge_sorted_lists(list_a, list_b))