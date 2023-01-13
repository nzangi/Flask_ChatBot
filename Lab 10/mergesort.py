def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    
    midpoint = int(len(unsorted_list)/ 2)

    left_list = merge_sort(unsorted_list[:midpoint])
    right_list = merge_sort(unsorted_list[midpoint:])

    return merge(left_list,right_list)


def merge(left_list, right_list):
    li = 0
    ri = 0
    result = []

    while li < len(left_list) and ri < len(right_list):
        if left_list[li] < right_list[ri]:
            result.append(left_list[li])
            li += 1
        else:
            result.append(right_list[ri])
            ri += 1
    
    result.extend(left_list[li:])
    result.extend(right_list[ri:])

    return result

def main():
    mylist = [9,8,7,6,5,4,1,0]
    print(mylist)
    sorted_list = merge_sort(mylist)
    print(sorted_list)


if __name__ == "__main__":
    main()