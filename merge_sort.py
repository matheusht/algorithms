def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: merge the sorted sublists created in previous step
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Takes O(log n) time
    """
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new merged list
    Takes O(n) space
    Runs in O(n) time
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[0] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < l(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


alist = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]
print(verify_sorted(alist))

"""
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half
    """
